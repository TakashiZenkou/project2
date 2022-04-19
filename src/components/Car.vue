<template>
    <div v-for="test in tests">
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        {{test.id}}
        {{test.price}}
        {{test.make}}
         <img :src="'/uploads/'+test.photo"/>
        <input type="submit" value="View more details" @click="open">
    </div>

    
</template>

<script>


export default({
    data() {
        return{
            csrf_token: '',
            tests: [],
        }    
    },
    created(){
        this.getCsrfToken();
        this.getCar();
    },
    methods:{
        getCar(){
            let self = this;
            fetch(`/api/cars/${self.$route.params.car_id}`,{
                method: 'Get',
                headers:{'Authorization': 'Bearer ' + localStorage.getItem('token')}
            })
            .then(function(response){
                return response.json();
            })
            .then(function(data){
                console.log(data)
                self.tests = data;
                console.log(self.tests)
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
        open(){
            let self = this;
            let fav = new FormData();
            fav.append('user_id',localStorage.getItem('id'));
            fav.append('car_id',`${self.$route.params.car_id}`);
            console.log(self.$route.params.car_id)
            fetch(`/api/cars/${self.$route.params.car_id}/favourite`,{
                method: 'Post',
                headers:{'Authorization': 'Bearer ' + localStorage.getItem('token')},
                body: fav,
                headers: {'X-CSRFToken' : this.csrf_token}
            })
            .then(function(response){
                return response.json();
            })
            .then(function(data){
                console.log(data)
            })
            .catch(function(error){
                console.log(error)
            })

        },
  }
})

</script>


<style scoped>
img{
    height:150px;
    width:50%;
}
</style>