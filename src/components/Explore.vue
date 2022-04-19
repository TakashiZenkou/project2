<template>
    <br>
    <br>
    <br>
    <form @submit.prevent="searchCar" class="d-flex flexcolumn justify-content-center">
    <div class="input-group mx-sm-3 mb-2">
    <label class="" for="make">Make</label>
    <input type="search" name="make" id="make" v-model="make" class="form-control mb-2 mr-sm-2"/>
    <label class="" for="model">Model</label>
    <input type="search" name="model" id="model" v-model="model" class="form-control mb-2 mr-sm-2"/>
    <button class="btn btn-primary mb-2">Search</button>
    </div>
    </form>
    <div v-for="car in cars" class="test">
        {{car.make}}
        {{car.model}}
        {{car.price}}
        <img :src="'/uploads/'+car.photo"/>
        <input type="submit" value="View more details" @click="move(car.car_id)">
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

img{
    height:150px;
    width:50%;
}
</style>
