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

    <div class="form-container">

    </div>
   
    <div class="card-container">
            <div class="cardDisplay">
                    <div v-for="car in cars" class="card cardBackground">
                        <img :src="'/uploads/'+car.photo" class="card-img-top">
                        <div class="card-body">
                            <div class="cardTitle">
                                <p class="h6">{{car.year}} {{car.make}}</p>
                                <div class="price-highlight">
                                    <span class="highlight"> {{"$" + parseFloat(car.price).toFixed(2)}} </span>
                                </div>
                                
                            </div>
                            <p>{{car.model}}</p>              
                        </div>
                        <div class="card-footer">
                            <input type="submit" value="View more details" @click="move(car.id)" class="btn">
                        </div>
                    </div>
            </div>
    </div>


</template>

<script>
import router from "../router";
import tagimg from '../assets/tag.png'

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
.tagimg{
    width: 5%;
    height: 5%;
}
.form-container{
    margin-left: 8%;
    margin-right: 8%;
}

.price-highlight{
    background-color:rgb(5, 143, 78);
    align-items: center;
    align-content: center;
    border-radius: 10px;
}
.highlight{
    font-size: small;
    color: white;
    border-radius: 10px;
    font-weight: bold;
    margin: 0;
    padding: 5px;
}

.btn{
    display: block;
	width: 100%;
    height: 100%;
    background-color: rgb(46, 96, 153);
    color: white;
}

.btn:hover{
    background-color: rgb(17, 48, 131);
}

.cardTitle{
    display: flex;
    justify-content: space-between;
}

.card-container{
    margin-left: 8%;
    margin-right: 8%;
}

.card-img-top {
    width: 100%;
    height: 15vw;
    object-fit: cover;
}

.cardDisplay{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.card{
    margin-top: 3%;
    flex: 0 1 calc(50%-1em);
}

.card{
    margin-top: 3%;
    flex: 0 1 calc(50%-1em);
}
</style>
