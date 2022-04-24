<template>
    <body>
        <div class="container-sm">
            <h2 class ="font-weight-bold">Add New Car</h2>
                <div v-if="verified" class="alert alert-success" role="alert" id="alert">
                    <p>{{ message }}</p>
                </div>
                <div v-else class="alert alert-danger" role="alert" id="alert">
                    <ul>
                        <li v-for="error in errors" class="error"> {{ error }} </li>
                    </ul>
                </div>
        <div class="card shadow p-3 mb-5">
            <form @submit.prevent="addCar" enctype="multipart/form-data" id = "addCarform">
            <div class="row mb-3">
                <div class="col-6">
                    <label for = "Make" class = "form-label font-weight-bold ">Make </label>
                    <input type ="text" placeholder="Enter Make" name = "Make" class = "form-control">
                    </div>
                <div class="col-6">
                    <label for = "Model" class ="form-label font-weight-bold" >Model </label>
                    <input type ="text" placeholder="Enter Model" name = "Model" class = "form-control">
                </div>
            </div>
            <div class="row mb-3">
                <div class="col">
                    <label for = "Colour" class ="font-weight-bold form-label">Colour </label>
                    <input type ="text" placeholder="Enter Colour" name = "Colour" class = "form-control">
                </div>
                <div class="col">
                    <label for = "Year" class ="font-weight-bold form-label">Year </label>
                    <input type ="text" placeholder="Enter Year" name = "Year" class = "form-control"    >
                </div>
            </div>
           <div class="row mb-3">
               <div class="col">
                    <label for = "Price" class ="font-weight-bold form-label">Price </label>
                    <input type ="text" placeholder="Enter Price" name = "Price" class = "form-control">
                </div>
                <div class="col">
                    <label for = "CarType" class ="font-weight-bold form-label">Car Type </label>
                    <select name="CarType" class="form-select">
                        <option selected>SUV</option>
                        <option value="1">Coupe</option>
                        <option value="2">Sedan</option>
                        <option value="3">Hatchback</option>
                        <option value="4">Station Wagon</option>
                        <option value="5">Pickup Truck</option>
                        <option value="5">Truck</option>

                    </select>

                </div>
            </div>

            <div class="row mb-3">
                <div class="col-6">
                    <label for = "Transmission" class = "font-weight-bold form-label">Transmission </label>
                    <select name="Transmission" class="form-select">
                        <option selected>Automatic</option>
                        <option value="1">Manual</option>
                    </select>

                </div>
            </div>
            

            <label for = "Description" class = "font-weight-bold form-label" >Description </label>
            <textarea name = "Description" placeholder="Enter Description" class = "form-control mb-3"></textarea>

            <label for = "photo" class = "font-weight-bold" >Upload Photo</label>
            <input type ="file" name = "photo" class = "form-control">
    
            <br>

            <button class="btn btn-success btn-md" type = 'submit'>Save</button>

        </form>
        </div>
    </div>

    </body>
</template>

<script>
import router from "../router";
export default ({
        data() {
            return{
            csrf_token: '',
            errors: [],
            message: '',
            verified: false

        }     
    },
    created(){
        this.getCsrfToken();
    },
    methods:{
        addCar(){
            let self = this;
            let carForm = document.getElementById("addCarform");
            let form_data = new FormData(carForm);
            var alertDiv = document.getElementById('alert');
            form_data.append('user_id',localStorage.getItem('id'))
            for (var [key, value] of form_data.entries()) { 
            console.log(key, value);
    }
            fetch('/api/cars',{
                method: 'POST',
                body: form_data,
                errors: [],
                message:'',
                verified: false,
                headers:{ 'X-CSRFToken' : this.csrf_token,
                'Authorization': 'Bearer ' + localStorage.getItem('token')
                }
            })
            .then(function(response){
                return response.json();
            })
            .then(function(data){
                console.log(data)
                
                alertDiv.style.display = 'block'
                if('message' in data){
                    self.message = data.message
                    self.verified = true;
                }

                if('errors' in data){
                    self.errors = [...data.errors];
                    self.verified = false;
                } else {
                    self.errors = [];
                    self.verified = true;
                }
                
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
        },
    }
})
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