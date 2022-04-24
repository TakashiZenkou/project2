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
        <button class = "btn btn-success">Email Owner</button>
        <input type="submit" value="Test" @click="open">
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
            tests: []
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
            console.log(self.$route.params.car_id)
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
</style>