<template>
  <div id="app">
    <div class="container-fluid bg-light">
      <div class="row vh-100">
        <nav class="col-md-2 d-none d-md-block bg-nicoe-blue sidebar">
          <div class="sticky-top">
            <div class="text-center py-1">
              <h3 class="text-white">EHR Code Mappings</h3>
            </div>
            <ul class="nav flex-column">
              <li class="nav-item">
                <router-link to="/" class="nav-link text-white h6">Home</router-link>
                <router-link to="/usage" class="nav-link text-white h6">Usage</router-link>
                <router-link to="/mappings" class="nav-link text-white h6">Mappings</router-link>
                <router-link to="/submit" class="nav-link text-white h6">Submit a Mapping</router-link>
              </li>
            </ul>

          </div>
        </nav>

        <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-4 mb-5 bg-light">
          <router-view class="p-2"/>
        </main>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
  .sidebar {
    border-right: 7px solid rgb(166, 25, 46) !important;
  }

  .sidebar .nav-link:hover {
    border-left: 5px solid white;
    font-weight: bold;
  }
</style>
