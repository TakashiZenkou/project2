<template>

<body>
<div class="container">

<div v-for="test in tests">
 <div class="card mb-3" style="max-width: 840px;">
  <div class="row g-0">
      <div class="col-md-4">
    <img :src="'/uploads/'+test.photo" class="img-fluid rounded-start carimg">
    </div>
    <div class="col-md-8">
        <div class="card-body">
            <h4 class="card-title">{{test.year}} {{test.make}}</h4>
            <h5 class="card-text text-muted">{{test.model}}</h5>
            <p class="card-text"><small class="text-muted">{{test.description}}</small></p>
        <div class = "cardetails">
            <div class = "carcolor">    
                <p class="font-weight-bold">Color <span class="normal">{{test.colour}} </span></p>
            </div>
            <div class ="cartype">
                <p class="font-weight-bold">Body Type <span class="normal"> {{test.car_type}} </span></p>
            </div>
        </div>
        <div class = "cardetails">
            <p class="font-weight-bold">Price <span class = "normal"> {{"$" + parseFloat(test.price).toFixed(2)}} </span> </p>
            <p class="font-weight-bold">Transmission <span class = "normal"> {{test.transmission}} </span> </p>
        </div>
        <div class = "buttom">   
            <button class = "btn btn-success">Email Owner</button>
        <button v-show ="!favourited" @click = "open" class = "fav">
            <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
            <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
            </svg>
        </button>
        <button v-show = "favourited" @click = "closed" class = "fav">
            <svg v-show ="favourited" xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="red" class="bi bi-heart-fill" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
            </svg>
        </button>
        </div>
        </div>
    </div>
  </div>
</div>
</div>

</div>
</body>
    
</template>

<script>


export default({
    data() {
        return{
            csrf_token: '',
            tests: [],
            favourited:false
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
                self.tests.push(data);
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
            fetch(`/api/cars/${self.$route.params.car_id}/favourite`,{
                method: 'POST',
                headers:{'Authorization': 'Bearer ' + localStorage.getItem('token'),
                'X-CSRFToken' : this.csrf_token},
                body: fav,
            })
            .then(function(response){
                return response.json();
            })
            .then(function(data){
                console.log(data)
                self.favourited = true;
            })
            .catch(function(error){
                console.log(error)
            })

        },
        closed(){
            this.favourited = false;
        }
  }
})

</script>


<style scoped>
img{
    height:150px;
    width:50%;
}

body{

    padding-top:175px;
}

.container{

    display: flex;
    justify-content: center;
    align-items: center;
}

.carimg{

    height:100%;
    width:100%;
}

.cardetails{

    display:grid;
	grid-template-columns: 200px 200px;


}

.font-weight-bold{

    color:grey;
}

.normal {

    color:black;
    padding-left: 20px;
}

h4 {

    font-weight: bold;
}

h5{
    font-weight: bold;
    color:grey;
    padding-bottom:5px;
}

.buttom{

    display: flex;
    justify-content: space-between;
    align-items: center;
}

.fav{

    border:none;
    background-color: white;
}
</style>