<template>
  <b-modal title="Sheet" id="sheet-details" size="xl" :ok-only="true" ok-title="Close" ok-variant="secondary"
           @shown="loadCodes">
    <div v-if="codes !== null">
      <b-form-input
        type="search"
        v-model="filters.search"
        size="sm"
        placeholder="Type to Search"
      ></b-form-input>

      <b-row class="mt-2">
        <b-col cols="4" v-if="hasClassification">
          <FilterBox title="Classifications" :values="allClassifications" v-model="filters.classifications"/>
        </b-col>
        <b-col cols="4" v-if="hasType">
          <FilterBox title="Types" :values="allTypes" v-model="filters.types"/>
        </b-col>
      </b-row>

      <div class="d-flex justify-content-end mb-2">
        <b-btn variant="nicoe-light-blue" size="sm">Download</b-btn>
      </div>
      <div class="d-flex justify-content-end">
        <span class="text-muted small">{{ codes.length.toLocaleString() }} codes</span>
      </div>
      <b-pagination
        v-model="pagination.current"
        :total-rows="numRows"
        :per-page="pagination.perPage"
      ></b-pagination>
      <b-table :fields="fields" :items="codes" class="text-center" :filter="filters" :filter-function="filterRow"
               :per-page="pagination.perPage"
               :current-page="pagination.current"
      >
      </b-table>
    </div>
  </b-modal>
</template>

<script>
  import Papa from "papaparse";
  import FilterBox from "@/components/FilterBox";

  export default {
    name: "Sheet",
    components: {FilterBox},
    props: ['id'],
    computed: {
      numRows() {
        return this.codes.length;
      },
      hasClassification() {
        if (this.codes === null)
          return false;

        const classifications = [...new Set(this.codes.map(row => row['Classification']))];
        return classifications.length > 1 || classifications[0] !== '';
      },
      hasType() {
        if (this.codes === null)
          return false;

        const types = [...new Set(this.codes.map(row => row['Type']))];
        return types.length > 1 || types[0] !== '';
      },
      fields() {
        if (this.codes === null)
          return [];

        let fields = [
          'Code',
          'Type',
          'Classification',
          'Description',
        ];

        if (!this.hasClassification) {
          fields.splice(fields.indexOf('Classification'), 1);
        }

        if (!this.hasType) {
          fields.splice(fields.indexOf('Type'), 1);
        }

        return fields;
      },
      allTypes() {
        const types = [...new Set(this.codes.map(item => item['Type']))];
        return types.map(t => ({
          title: t,
          count: this.codes.filter(item => item['Type'] === t).length,
        }));
      },
      allClassifications() {
        const classifications = [...new Set(this.codes.map(item => item['Classification']))];
        return classifications.map(c => ({
          title: c,
          count: this.codes.filter(item => item['Classification'] === c).length,
        }));
      },
    },
    data() {
      return {
        pagination: {
          current: 1,
          perPage: 15,
        },
        codes: null,
        filters: {
          search: null,
          types: [],
          classifications: [],
        },
      }
    },
    methods: {
      filterRow(item, filters) {
        if (filters.search !== null && filters.search !== '') {
          let attribs = ['Code', 'Description'];
          attribs = attribs.filter(attrib => item[attrib].toUpperCase().includes(filters.search.toUpperCase()));
          if (attribs.length === 0)
            return false;
        }

        if (this.hasClassification && !filters.classifications.includes(item['Classification']))
          return false;

        if (this.hasType && !filters.types.includes(item['Type']))
          return false;

        return true;
      },
      loadCodes() {
        let component = this;
        Papa.parse('sheets/' + this.id + '.csv', {
          download: true,
          header: true,
          skipEmptyLines: true,
          complete: function (results) {
            component.codes = results.data;
            if (component.hasClassification)
              component.filters.classifications = component.allClassifications.map(item => item.title);

            if (component.hasType)
              component.filters.types = component.allTypes.map(item => item.title);
          }
        });
      },
    },
  }
</script>

<style scoped>

</style>