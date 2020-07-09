<template>
  <span>
    <b-btn href="#" size="xs" :id="title + '-target'" class="ml-1" variant="light">
      <font-awesome-icon icon="filter" :class="indeterminate ? 'text-nicoe-light-blue' : 'text-secondary'"/>
    </b-btn>
    <b-popover :target="title + '-target'" triggers="focus" placement="bottom">
      <b-card no-body class="filter-content overflow-auto p-2 border-0">
        <b-input type="search" size="sm" class="mb-2" v-model="search"/>
        <b-form-checkbox v-model="allSelected" :indeterminate="indeterminate" @change="toggleAll">
          {{ allSelected ? 'Select None' : 'Select All' }}
        </b-form-checkbox>
        <b-form-checkbox-group stacked v-model="filters">
          <b-form-checkbox v-for="item in searchedValues" :value="item.title">
            {{ item.title }} <span class="text-muted small">({{ item.count }})</span>
          </b-form-checkbox>
        </b-form-checkbox-group>
      </b-card>
    </b-popover>
  </span>
</template>

<script>
  export default {
    name: "FilterBox",
    props: ['title', 'values', 'value'],
    data() {
      return {
        search: null,
      }
    },
    computed: {
      filters: {
        get() {
          return this.value;
        },
        set(value) {
          this.$emit('input', value);
        },
      },
      allSelected: {
        get() {
          return this.filters.length === this.values.length;
        },
        set(value) {
          //Do nothing
        },
      },
      indeterminate() {
        return this.filters.length !== 0 && this.filters.length !== this.values.length;
      },
      searchedValues() {
        console.log('searchedValues', this.search);
        if (this.search === null || this.search === '')
          return this.values;

        return this.values.filter(value => value.title.toUpperCase().includes(this.search.toUpperCase()));
      },
    },
    methods: {
      toggleAll(value) {
        if (value)
          this.$emit('input', this.values.map(item => item.title));
        else
          this.$emit('input', []);
      },
    },
  }
</script>

<style scoped>
  .filter-content {
    max-height: 250px;
  }
</style>