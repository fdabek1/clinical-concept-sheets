<template>
  <div class="about">
    <h2 class="mb-4">Mappings</h2>
    <div v-if="mappings !== null">

      <b-form-tags
        v-model="filters.tags"
        separator=" "
        placeholder="Filter by tags"
        remove-on-delete
        :tag-validator="tagValidator"
        class="mb-2"
      ></b-form-tags>

      <b-table striped hover :fields="fields" :items="mappings" class="text-center"
               :filter="filters" :filter-function="filterRow">

        <template v-slot:cell(Tags)="row">
          <b-badge v-for="tag in row.value" class="mr-1">{{ tag }}</b-badge>
        </template>

        <template v-slot:cell(Preview)="row">
          <b-button size="xs" @click="info(row.item)" class="mr-1">
            Preview
          </b-button>
        </template>

      </b-table>

      <b-modal ref="mappingInfo" ok-only title="Loading..." size="lg" @hide="resetSelected">
        <template slot="modal-title" v-if="selected.item !== null">
          {{ selected.item['Title'] }}
        </template>
        <div v-if="selected.item !== null">
          <div class="jumbotron p-4">
            <p v-if="selected.item['Description'] === ''" class="text-muted">N/A</p>
            <p v-else v-html="selected.item['Description']"></p>
          </div>
          <h5>Preview</h5>
          <span v-if="selected.data === null">Loading...</span>
          <b-table v-else :items="selected.data"></b-table>
        </div>
      </b-modal>
    </div>
  </div>
</template>
<script>
  import Papa from "papaparse";

  export default {
    name: 'Mappings',
    computed: {
      authors() {
        return [...new Set(this.mappings.map(row => row['Author']))];
      },
      tags() {
        let tags = [];
        for (let row of this.mappings) {
          for (let tag of row['Tags']) {
            tags.push(tag);
          }
        }

        return tags;
      },
    },
    data() {
      return {
        mappings: null,
        selected: {
          item: null,
          data: null,
        },
        fields: [
          'ID',
          'Author',
          'Author Email',
          'Title',
          'Tags',
          'CurrentVersion',
          'Preview',
        ],
        filters: {
          tags: [],
        },
      }
    },
    methods: {
      tagValidator(tag) {
        return this.tags.filter(t => t === tag).length > 0;
      },
      filterRow(item, filter) {
        if (filter.tags.length === 0)
          return true;

        if (filter.tags.length > 0) {
          for (let tag of filter.tags) {
            if (item['Tags'].includes(tag))
              return true;
          }
        }

        return false;
      },
      info(item) {
        this.selected.item = item;
        this.loadSelectedData();
        this.$refs['mappingInfo'].show();
      },
      resetSelected() {
        this.selected.item = null;
        this.selected.data = null;
      },
      loadSelectedData() {
        let component = this;
        const filename = this.selected['Title'] + '.v' + this.selected['CurrentVersion'] + '.csv';
        Papa.parse('https://cdn.jsdelivr.net/gh/fdabek1/ehr-code-mappings/mappings/' + filename, {
          download: true,
          header: true,
          skipEmptyLines: true,
          complete: function (results) {
            component.selected.data = results.data;
          }
        });
      },
    },
    mounted() {
      let component = this;
      Papa.parse('https://cdn.jsdelivr.net/gh/fdabek1/ehr-code-mappings/mappings.csv', {
        download: true,
        header: true,
        skipEmptyLines: true,
        complete: function (results) {
          results.data = results.data.map(row => {
            row['Tags'] = row['Tags'].split(',');
            return row;
          });
          component.mappings = results.data.slice(0, 500);
        }
      });
    },
  }
</script>
