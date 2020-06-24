<template>
  <div>
    <h2 class="mb-4">Usage</h2>

    <vue-code-highlight>
      load_mapping(name, version=None)
    </vue-code-highlight>

    <ul>
      <li><strong>name:</strong> The name/ID of the mapping</li>
      <li><strong>version:</strong> Specify the version of the mapping to load (Optional, by default loads the latest
        mapping)
      </li>
    </ul>


    <p>To install:</p>
    <vue-code-highlight>
      pip install ehr-code-mappings
    </vue-code-highlight>

    <h4 class="my-4">Examples</h4>

    <vue-code-highlight>
      <pre>
import ehr_code_mappings as mappings

result = mappings.load_mapping('ccs_icd10')
print(result.head())</pre>
    </vue-code-highlight>
    <div class="mt-3 w-50">
      <table class="table text-center">
        <thead>
        <tr>
          <th scope="col">Code</th>
          <th scope="col">Single</th>
          <th scope="col">Level1</th>
          <th scope="col">Level2</th>
        </tr>
        </thead>
        <tbody>
        <tr>
          <th>A000</th>
          <td>135</td>
          <td>9</td>
          <td>9.1</td>
        </tr>
        <tr>
          <th>A001</th>
          <td>135</td>
          <td>9</td>
          <td>9.1</td>
        </tr>
        <tr>
          <th>A009</th>
          <td>135</td>
          <td>9</td>
          <td>9.1</td>
        </tr>
        <tr>
          <th>A0100</th>
          <td>135</td>
          <td>9</td>
          <td>9.1</td>
        </tr>
        <tr>
          <th>A0101</th>
          <td>76</td>
          <td>6</td>
          <td>6.1</td>
        </tr>
        </tbody>
      </table>
    </div>

    <br>
    <br>
    <br>

    <vue-code-highlight>
      <pre>
import ehr_code_mappings as mappings

result = mappings.load_mapping('ccs_icd10')
result = result[result['Level2'] == '2.15']
codes = result['Code'].values.tolist()
print(codes)</pre>
    </vue-code-highlight>
    <div class="alert alert-secondary mt-3" role="alert">
      ['Z510', 'Z5111', 'Z5112']
    </div>
  </div>
</template>

<script>
  import {component as VueCodeHighlight} from 'vue-code-highlight';
  import "vue-code-highlight/themes/prism-tomorrow.css";

  export default {
    name: "Usage",
    components: {
      VueCodeHighlight,
    },
  }
</script>

<style scoped>

</style>