<template>
    <br>
    <br>
    <br>
    
    <div class="container card">
        <form @submit.prevent="searchCar" class="form-control">
                <div class="carDetails form-inline">
                    <label for="make">Make</label> <br>
                    <input type="search" name="make" v-model="make">
                </div>

                <div class="carDetails form-inline">
                    <label for="model">Model</label> <br>
                    <input type="search" name="model" v-model="model">
                </div>

                <div class="form-inline">
                    <button class="btn btn-primary mb-2">Search</button>
                </div>
        </form> 
    </div>
   
   <div class="container">

       <div v-for="car in cars" class="test">
        {{car.make}}
        {{car.model}}
        {{car.price}}
        <img :src="'/uploads/'+car.photo" class="pfp"/>
        <input type="submit" value="View more details" @click="move(car.id)">
    </div>
   </div>
</template>

<script>
import router from "../router";
export default({
    data() {
        return{
            make: '',
            model: '',
            cars: [],
        }    
    },
    created(){
            this.getCsrfToken();
            this.getCars();
    },
    
    methods: {
        getCars(){
            let self = this;
            fetch('/api/cars',{
                method: 'Get',
                headers: {'Authorization': 'Bearer ' + localStorage.getItem('token')}
            })
            .then(function(response){
                console.log("test")
                return response.json();
            })
            .then(function(data){
                console.log(data)
                self.cars = data;
                console.log(self.cars)
            })
            .catch(function(error){
                console.log(error)
            });
        },
            move(car_id){
                router.push(`/cars/${car_id}`)
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
            searchCar(){
                let self = this;
                fetch('/api/search?model='+self.model +'&make='+self.make,{
                    headers:{'Authorization': 'Bearer ' + localStorage.getItem('token')}
                })
                .then(function(response){
                    return response.json();
                })
                .then(function(data){
                    console.log(data);
                    self.cars = data;
                })
                .catch(function(error){
                    console.log(error)
                })
            }
    }
})
</script>

<style scoped>
.test{
    height: 400px;
    width:300px;
}

.pfp{
    height:150px;
    width:50%;
}

/* .container { 
    display: flex;
    flex-wrap: wrap;
    background-color:blueviolet;
} */

form {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
    align-content: center;
    margin: 10px;
}

.card {
    width: 800px;
    align-items: center;
    padding: 20px;
}

button {
  margin-left: 15px;
}

.btn-primary {
    background-color: aquamarine;
}

.btn {
    display: flex;
}
.carDetails {
    margin-left: 40px;
}
</style>
