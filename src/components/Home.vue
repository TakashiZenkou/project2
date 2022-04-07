<template>
<div class="container">
    <div class="row">
        <div class="col-6">
            <h1 class ="text-align-center">Buy and Sell Cars Online</h1>
            <p>United Auto Sales provides the fastest easiest and 
                most user friendly way to buy or sell cars online.
                Find a great price on the Vehicle You Want!
            </p>
            <button @click = "Register">Register</button>
            <button @click = "Login">Login</button>
        </div>
        <div class="col-md-6">
            <img class = "" :src = "image">
        </div>
        </div>

</div>
</template>

<script>

import homeimg from '../assets/HomePage.png'
export default{

    data(){

        return {image : homeimg}
    },

methods:
{
    Register(){
        this.$router.push('/register');
    },

    Login(){
        this.$router.push('/login');
    }
}
}
</script>

<style scoped>

.homeimg {
    
  width: 1000px;
  height:100%;
}

* {

    margin:0px;
    padding:0px;
    box-sizing: border-box;

}

</style>