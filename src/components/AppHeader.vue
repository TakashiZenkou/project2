<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">
        <img src = "../assets/HeaderIcon.png" width="25">  
        United Auto Sales</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
            <li v-if = "!logged_in" class="nav-item ">
              <RouterLink class="nav-link" to="/register">Register</RouterLink>
            </li>
            <li v-if = "!logged_in" class="nav-item">
              <RouterLink @click = "Logout" class="nav-link" to="/login">Login</RouterLink>
            </li>
            <li v-if = "logged_in" class="nav-item">
              <RouterLink class="nav-link" to="/cars/new">Add Cars</RouterLink>
            </li>
            <li v-if = "logged_in" class="nav-item">
              <RouterLink class="nav-link" to="/logout">Logout</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>

export default {

  data(){

    return {null:null}
  },

  computed : {

          logged_in: function() {
            if (localStorage.getItem('token')) {
                return true;
            } else {
                return false;
            }
        }
    }

  }


</script>

<style scoped>
.navbar-brand{

  font-size: 16px;

}


</style>