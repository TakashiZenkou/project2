<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container-fluid">
        <span v-if="!logged_in" class="navbar-brand" >
        <img src = "../assets/HeaderIcon.png" width="25">  
        United Auto Sales </span>

        <span v-if="logged_in" class="navbar-brand">
        <img src = "../assets/HeaderIcon.png" width="25">  
        United Auto Sales</span>
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
              <RouterLink class="nav-link" to="/login">Login</RouterLink>
            </li>
            <li v-if = "logged_in" class="nav-item">
              <RouterLink class="nav-link" to="/cars/new">Add Cars</RouterLink>
            </li>
            <li v-if = "logged_in" class="nav-item">
              <RouterLink class="nav-link" to="/explore">Explore</RouterLink>
            </li>
            <li v-if = "logged_in" class="nav-item">
              <RouterLink class="nav-link" :to= '"/users/"+ id' >My Profile</RouterLink>
            </li>
            <li v-if = "logged_in" class="nav-item">
              <RouterLink class="nav-link" @click = "Logout" to="/login">Logout</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>

import router from "../router";

export default {

  data(){

    return {null:null,
      id: ''
    }
  },

  computed : {

          logged_in: function() {
            if (localStorage.getItem('token')) {
                return true;
            } else {
                return false;
            }
        }
    },
  methods:{

        Logout(){

        let self = this;
        fetch('/api/auth/logout', 
        { method: 'POST', 
        headers: { 'Authorization': 'Bearer ' + localStorage.getItem('token'),
                    'X-CSRFToken' : this.csrf_token,
        }})
        .then(function (response) {
            return response.json();
        })
        .then(function(data) {
            console.log(data);
            localStorage.removeItem('token');
            localStorage.removeItem('id');
            console.info('Token removed from localstorage');
            router.push("/")
                })
    },
    getCsrfToken(){
            let self = this;
            fetch('/api/csrf-token')
            .then((response)=>response.json())
            .then((data)=>{
                console.log(data);
                self.csrf_token = data.csrf_token;
            })
        },

    Profile(){
      let self = this;
      self.id = localStorage.getItem('id')
      console.log(self.id)
    },
    },
    created(){
    this.Profile();
    this.getCsrfToken();
    }

  }


</script>

<style scoped>
.navbar-brand{

  font-size: 16px;

}


</style>