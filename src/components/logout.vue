<template>
<body>
    <p> Logging Out</p>
</body>
</template>

<script>

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
        headers: { 'Authorization': 'Bearer ' + localStorage.getItem('token')}})
        .then(function (response) {
            return response.json();
        })
        .then(function(response) {
            let result = response.data;
            alert(result.user.username + " logged out!")
            localStorage.removeItem('token');
            console.info('Token removed from sessionStorage.');
            router.push("/")
                })
        .catch(function (error) {
            console.log(error);
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
    },

    beforeMount(){

    this.getCsrfToken()
    this.Logout()
    
    }
};



</script>

<style scoped>

body{

    margin-top:75px;
}

</style>