<template>

<body>

    <div class="container-sm">
        <h2 class ="font-weight-bold">Register New User</h2>

        <div v-if="verified" class="alert alert-success" role="alert" id="alert">
            <p>{{ message }}</p>
        </div>
        <div v-else class="alert alert-danger" role="alert" id="alert">
            <ul>
                <li v-for="error in errors" class="error"> {{ error }} </li>
            </ul>
        </div>

        <div class="card shadow p-3 mb-5">
            <form @submit.prevent="Registration" enctype="multipart/form-data" id = "registrationform">
            <div class="row mb-3">
                <div class="col-6">
                    <label for = "username" class = "form-label font-weight-bold ">Username </label>
                    <input type ="text" placeholder="Enter username" name = "username" class = "form-control">
                    </div>
                <div class="col-6">
                    <label for = "password" class ="form-label font-weight-bold" >Password </label>
                    <input type ="password" placeholder="Enter password" name = "password" class = "form-control">
                </div>
            </div>
            <div class="row mb-3">
                <div class="col">
                    <label for = "fullname" class ="font-weight-bold form-label">Fullname </label>
                    <input type ="text" placeholder="Enter fullname" name = "fullname" class = "form-control">
                </div>
                <div class="col">
                    <label for = "email" class ="font-weight-bold form-label">Email </label>
                    <input type ="email" placeholder="Enter email" name = "email" class = "form-control"    >
                </div>
            </div>

            <div class="row mb-3">
                <div class="col-6">
                    <label for = "location" class = "font-weight-bold form-label">Location </label>
                    <input type ="text" placeholder="Enter fullname" name = "location" class = "form-control">
                </div>
            </div>
            

            <label for = "biography" class = "font-weight-bold form-label" >Biography </label>
            <textarea name = "biography" placeholder="Enter bio" class = "form-control mb-3"></textarea>

            <label for = "photo" class = "font-weight-bold" >Upload Photo</label>
            <input type ="file" name = "photo" class = "form-control">
    
            <br>

            <button class="btn btn-success btn-md" type = 'submit'>Register</button>

        </form>
        </div>
    </div>
    </body>

</template>

<script>

import router from "../router";

export default{
    data(){
        return {
            csrf_token : '',
            errors: [],
            message: '',
            verified: false
        }
    },
    created(){
        this.getCsrfToken();
    },
    methods:
    {
  
        Registration(){
            let uploadForm = document.getElementById('registrationform');
            var alertDiv = document.getElementById('alert');
            let form_data = new FormData(uploadForm);
            let self = this
            fetch("api/register",{
                method: 'POST',
                body: form_data,
                errors: [],
                message:'',
                verified: false,
                headers:{
                    'X-CSRFToken' : this.csrf_token
                }
            })
            .then(function(response){
                
                return response.json()
            })
            .then(function(data){

                alertDiv.style.display = 'block'
                if('message' in data){
                    console.log(data)
                    self.message = data.message
                    self.verified = true;
                    router.push('/login')
                }

                if('errors' in data){
                    self.errors = [...data.errors];
                    self.verified = false;
                } else {
                    self.errors = [];
                    self.verified = true;
                    router.push('/login')
                }

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
.alert{
    display:none;
}
.container-sm{


    width:40%;
    box-shadow: 2px;
    background-color: rgb(226, 223, 223);

}

textarea{
    
    resize: none;
}

.card {
    margin-top:40px;
    padding:40px;
    border-radius: 15px;
    background-color: white;

}

h2{

    margin-top: 20px;
}

*{

    font-family: sans-serif;
}

.font-weight-bold{

    font-weight: bold;
}

body{
  padding-top: 75px;
}
</style>