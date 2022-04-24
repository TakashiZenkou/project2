<template>
<div class="container">
    <div class="profilec d-flex flex-column justify-content-center ">
        <div v-if="a" v-for="user in users" class="profile shadow p-3 mb-5 bg-white rounded border-2">
            <div class="img">
                <img class="profileimg" :src="'../uploads/'+user.photo" alt="Card image cap">
            </div>
            <div class="lel">
                <div class="back">
                    <p class="name">{{user.name}}</p>
                    <p class="username text-secondary">{{"@" +user.username}}</p>
                </div>
                <p class="bio text-secondary">{{user.biography}}</p>
                <dl class ="row">       
                    <dt class= "col-sm-3 text-secondary">Email</dt>  
                    <dd class="col-sm-9 "> {{user.email}} </dd>
                    <dt class= "col-sm-3 text-secondary">Location</dt>  
                    <dd class="col-sm-9 "> {{user.location}} </dd>
                    <dt class= "col-sm-3 text-secondary">Joined</dt>  
                    <dd class="col-sm-9"> {{user.date_joined}} </dd>
                </dl>
            </div>
        </div>
    </div>
    <h1> Cars Favourited </h1>
        <div class="row row-cols-1 row-cols-md-3 g-2" style="width:800px;"> 
            <div v-if="b" v-for="car in cars" class="col col-4">
                <div class="card rounded" style="height:370px;">
                    <img class="card-img-top" :src="'uploads/'+car.photo" alt="Card image cap">
                    <div class="card-body">
                    <p class="card-title me-0;">{{car.year}} {{car.make}} <span> <button type="button" class="price">{{"$" + parseFloat(car.price).toFixed(2)}}</button> </span></p>
                    <p class="card-text text-secondary fw-bold">{{car.model}}</p>
                    </div>
                    <button @click="move(car.id)" type="button" class="btnsmall align-self-center btn btn-block btn-primary mt-auto mb-2">View More Details</button>
                </div>
            </div>
        </div>
</div>
</template>


<script>
import router from "../router";
export default {
    data() {
        return{
            cars: [],
            users: [],
            a: false,
            b: false,
        }
        
    },
    created(){
        this.getCsrfToken();
        this.getFavs();
        this.getUser();
    },
    methods:{
        getFavs(){
            let self = this;
            fetch(`/api/users/${self.$route.params.user_id}/favourites`, {
                method:'Get',
                headers:{'Authorization': 'Bearer ' + localStorage.getItem('token')}
            })
            .then(function(response){
                return response.json();
            })
            .then(function(data){
                console.log(data)
                self.cars = data;
                console.log(self.cars)
                if (Array.isArray(self.cars)) {
                    self.b = true;
                }
            })
            .catch(function(error){
                console.log(error)
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
        },
            getUser(){
                let self = this;
                fetch(`/api/users/${self.$route.params.user_id}`,{
                    method:'Get',
                    headers: {'Authorization': 'Bearer ' + localStorage.getItem('token')}
                })
                .then(function(response){
                    return response.json()
                })
                .then(function(data){
                    console.log(data)
                    self.users.push(data);
                    if ("id" in self.users[0]){
                    self.a = true;
                 }
                })
                .catch(function(error){
                    console.log(error)
                })
            },
            move(car_id){
                let self = this;
                router.push(`/cars/${car_id}`)
            }
    }
}
</script>


<style>
.profile{
    width: 800px;
    height: 330px;
    margin-top:7em;
    display:flex;
    flex-direction: row;
    margin-bottom:4em;
    background-color:white;
}

.profileimg{
    margin-left:1em;
    width:150px;
    height:150px;
    object-fit: cover;
    border-radius: 50%;
}

.container{
    overflow: scroll;
    display:flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.card-img-top{
    width:100%;
    height:200px;
    object-fit: cover;
}



div.lel > p{
    margin-top:1em;
    margin-bottom:0em;
}



.name{
    font-weight:700;
    font-size:30px;
    margin-bottom:0em;
}

.username{
    margin-bottom:0em;
    color:rgb(170, 168, 168);
    font-weight:600;
}

.lel{
    margin-left:2.5em;
    width:75%;
}


dl{
    margin-top:1em !important; 
    font-weight:600;
}

.bio{
    margin-right:10em;
    font-size:15px;
    font-weight:600;
}

h1{
    margin-bottom: 1em;
    margin-right: 12em;
}
.btnsmall{
    width:85%;
    padding-top:.3em;
    padding-bottom: .3em;
}

.card-body{
    font-size: 15px;
    padding: .5rem .5rem;
    font-weight:500;
    padding-right:0em;
}

.price{
    background-color:rgb(24,179,129);
    width:fit-content;
    color:white;
    padding: 5px 8px;
    text-align: center;
    border:none;
    border-radius: 8px;
    margin-right:.5em;
    font-size: 12px;
    font-weight: 600;
    float:right;
}
</style>