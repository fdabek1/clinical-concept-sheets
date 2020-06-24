<template>
  <div class="home">
    <h1 class="display-4">Clinical Concept Sheets</h1>
    <div v-if="sheets !== null">

      <b-form-input
        type="search"
        v-model="filters.search"
        size="sm"
        placeholder="Type to Search"
      ></b-form-input>

      <b-row class="mt-2">
        <b-col cols="4">
          <FilterBox title="Concepts" :values="allConcepts" v-model="filters.concepts"/>
        </b-col>
        <b-col cols="4">
          <FilterBox title="Tags" :values="allTags" v-model="filters.tags"/>
        </b-col>
      </b-row>

      <div class="d-flex justify-content-end">
        <span class="text-muted small">{{ sheets.length.toLocaleString() }} sheets</span>
      </div>

      <b-table :fields="fields" :items="sheets" class="text-center" :filter="filters" :filter-function="filterRow">
        <template v-slot:cell(Version)="data">
          {{ data.item['MajorVersion'] }}.{{ data.item['MinorVersion'] }}
        </template>

        <template v-slot:cell(Tags)="data">
          <b-badge v-for="tag in data.value" class="mr-2">{{ tag }}</b-badge>
        </template>

        <template v-slot:cell(LastModified)="data">
          {{ new Date(data.value).toLocaleDateString() }}
        </template>

        <template v-slot:cell(Go)="data">
          <b-btn size="sm" variant="nicoe-light-blue" @click="openDetails(data.item['ID'])">View Details</b-btn>
        </template>

      </b-table>
    </div>
    <Sheet ref="modal" :id="selected === null ? null : selected['ID']" :details="selected"/>
  </div>
</template>

<script>
  import Papa from "papaparse";
  import Sheet from "@/components/Sheet";
  import FilterBox from "@/components/FilterBox";

  export default {
    name: 'Home',
    components: {
      FilterBox,
      Sheet,
    },
    computed: {
      allConcepts() {
        const concepts = [...new Set(this.sheets.map(sheet => sheet['Concept']))];
        return concepts.map(concept => ({
          title: concept,
          count: this.sheets.filter(sheet => sheet['Concept'] === concept).length,
        }));
      },
      allTags() {
        const tags = [...new Set(this.sheets.map(sheet => sheet['Tags']).flat())];
        return tags.map(tag => ({
          title: tag,
          count: this.sheets.filter(sheet => sheet['Tags'].includes(tag)).length,
        }));
      },
    },
    data() {
      return {
        sheets: null,
        selected: null,
        fields: [
          'Concept',
          'Description',
          'Tags',
          {
            key: 'Author',
            title: 'POC'
          },
          'Version',
          {
            key: 'LastModified',
            title: 'Last Modified'
          },
          'Go'
        ],
        filters: {
          search: null,
          concepts: [],
          tags: [],
        },
      }
    },
    mounted() {
      let component = this;
      Papa.parse('sheets.csv', {
        download: true,
        header: true,
        skipEmptyLines: true,
        complete: function (results) {
          component.sheets = results.data.map(row => {
            row['Tags'] = row['Tags'].split(',');
            return row;
          });
          component.filters.concepts = component.allConcepts.map(concept => concept.title);
          component.filters.tags = component.allTags.map(tag => tag.title);
        }
      });
    },
    methods: {
      filterRow(item, filters) {
        if (filters.search !== null && filters.search !== '') {
          let attribs = ['Author', 'Concept', 'Description'];
          attribs = attribs.filter(attrib => item[attrib].toUpperCase().includes(filters.search.toUpperCase()));
          if (attribs.length === 0)
            return false;
        }

        if (!filters.concepts.includes(item['Concept']))
          return false;

        if (!item['Tags'].some(tag => filters.tags.includes(tag)))
          return false;

        return true;
      },
      openDetails(id) {
        this.selected = this.sheets.find(sheet => sheet['ID'] === id);
        this.$root.$emit('bv::show::modal', 'sheet-details');
      },
    },
  }
</script>

