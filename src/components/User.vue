<template>
    <div>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        Hi
    </div>
    <div v-for="user in users">
        {{user.name}}
    </div>
    <div v-for="car in cars">
        {{car.make}}
        {{car.model}}
        {{car.price}}
        <img :src="'/uploads/'+car.photo" class="pfp"/>
    </div>
</template>


<script>
export default {
    data() {
        return{
            cars: [],
            users: [],
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
                    console.log(self.users)
                })
                .catch(function(error){
                    console.log(error)
                })
            }
    }
}
</script>


<style>

</style>