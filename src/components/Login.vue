<template>
<body>

    <div class="container">
        <h2 class ="font-weight-bold text-center">Login to your account</h2>
        <div class="card">
            <form @submit.prevent="Login" enctype="multipart/form-data" id = "loginform">
            <div class="row mb-3">
                <label for ="username" class = "form-label font-weight-bold ">Username</label>
                <input type = "text" class ="form-control" name = "username" placeholder="Enter Username">
            </div>
            <div class="row mb-3">
                <label for = "password" class = "form-label font-weight-bold ">Password</label>
                <input type = "password" class ="form-control" name = "password" placeholder="Enter Password">
            </div>
            <div class="row">
                <button type = "submit" class = "btn btn-success mt-3">Login</button>
            </div>
        </form>
        </div>


    </div>

            </body>
</template>

<script>

export default{

    data(){

    return {csrf_token: ''}

    },
    created(){
        this.getCsrfToken();
    },
    methods:
    {
    Login(){

        let uploadForm = document.getElementById('loginform');
        let form_data = new FormData(uploadForm);

        console.log(form_data)
         fetch("api/auth/login",{
                method: 'POST',
                body: form_data,
                headers:{
                    'X-CSRFToken' : this.csrf_token
                }
            })
            .then(function(response){
                
                return response.json()
            })
            .then(function(data){
                console.log(data)
            })
            .catch(function(error){
                console.log(error)
            });
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


    }

    }
</script>

<style scoped>

.container{

    width:30%;
    box-shadow: 2px;
    background-color: rgb(226, 223, 223);
    margin-top: 90px;
}

.card {
    
    margin-top:40px;
    padding:40px;
    border-radius: 12px;
    background-color: white;

}   

.font-weight-bold{

    font-weight: bold;
}

body{
  padding-top: 75px;
}
</style>