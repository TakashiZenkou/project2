<template>
<div class="container">
    <div v-if="a" v-for="user in users" class="profile shadow p-3 mb-5 bg-white rounded">
        <div class="img">
            <img class="test" :src="'/uploads/'+user.photo" alt="Card image cap">
        </div>
        <div class="lel">
            <div class="back">
                <p class="info">{{user.name}}</p>
                <p>{{"@" +user.username}}</p>
                <button class="btn">{{user.price}}</button>
            </div>
            <p>{{user.biography}}</p>
            <div class="front">
                <p>Email: {{user.email}} </p>
                <p>Location: {{user.location}} </p>
                <p>Date Joined: {{user.date_joined}} </p>
            </div>
        </div>
    </div>
    <h1> Cars Favourited </h1>
    <div class="card-deck d-flex flex-column flex-md-row align-items-center">
        <div v-if="b" v-for="car in cars" class="card mx-2">
        <img class="card-img-top" :src="'/uploads/'+car.photo" alt="Card image cap">
        <div class="card-body flex-column d-flex h-50">
        <h5 class="card-title"> {{car.year}} {{car.make}}</h5>
        <p class="card-text">{{car.model}}</p>
        </div>
        <div class="card-footer">
        <button type="button" class="align-self-center btn btn-lg btn-block btn-primary mt-auto">View More Details</button>
        </div>
    </div>
 </div>
</div>
</template>


<script>
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
            }
    }
}
</script>


<style>
.profile{
    width: 700px;
    height: 300px;
    margin-top:7em;
    display:flex;
    flex-direction: row;
    margin-bottom:4em;
    background-color:white;
}

.container{
    display:flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.card-img-top{
    width:300px;
    height:277px;
}

.test{
    margin-left:1em;
    margin-top:2em;
    width:150px;
    height:150px;
    object-fit: cover;
    border-radius: 50%;
}

div.lel > p{
    margin-left:2em;
    margin-top:1em;
    margin-bottom:0em;
    font-weight: 400;
}
.back{
    margin-top:1em;
    margin-left:2em;
}

.front{
    margin-top:2em;
    margin-left:2em;
}

div.front >p {
    font-size: 14px;
    font-weight:600;
}

.info{
    font-weight:600;
    font-size:20px;
}

div.back >p{
    margin-bottom:0em;
}
</style>