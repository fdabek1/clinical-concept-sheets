<template>
  <b-card body-class="filter-content overflow-auto pt-3" :header="title" header-tag="h6">
    <b-form-checkbox v-model="allSelected" :indeterminate="indeterminate" @change="toggleAll">
      {{ allSelected ? 'Select None' : 'Select All' }}
    </b-form-checkbox>
    <b-form-checkbox-group stacked v-model="filters">
      <b-form-checkbox v-for="item in values" :value="item.title">
        {{ item.title }} <span class="text-muted small">({{ item.count }})</span>
      </b-form-checkbox>
    </b-form-checkbox-group>
  </b-card>
</template>

<script>
  export default {
    name: "FilterBox",
    props: ['title', 'values', 'value'],
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