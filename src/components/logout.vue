<template>
<body>
    <button @click = "Logout">Logout</button>
</body>
</template>

<script>

import router from "../router";

export default{


    data(){

    return {csrf_token: ''}

    },
    methods:
    {
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
        }
    },
    created(){
    this.getCsrfToken()
    },
};



</script>

<style scoped>

body{

    margin-top:75px;
}

</style>