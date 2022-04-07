<template>

<body>
        <img :src = "image" class = 'homeimg'>



</body>

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

* {
    
    margin:0px;
    padding:0px;
    box-sizing: border-box;

}


</style>