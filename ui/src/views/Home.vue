<template>
  <div class="home">
    <div class="jumbotron">
      <h1 class="display-4">EHR Code Mappings</h1>
      <p class="lead">Welcome to EHR Code Mappings!</p>
      <hr class="my-4">
      <p>To install:</p>
      <vue-code-highlight>
        pip install ehr-code-mappings
      </vue-code-highlight>
    </div>
  </div>
</template>

<script>
  import {component as VueCodeHighlight} from 'vue-code-highlight';
  import "vue-code-highlight/themes/prism-tomorrow.css";

  export default {
    name: 'Home',
    components: {
      VueCodeHighlight,
    },
  }
</script>
