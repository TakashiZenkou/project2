<template>

    <body>
            <div class = 'home-page'>

                <div class = "middle">
                    
                    <h2> Buy and Sell Cars Online </h2>
    <p> United Auto Sales provides the fastest, easiest and most user friendly way to buy or sell cars online.
        Find a great price on a vehicle you want.
    </p>
        </div>
        
    <button @click="Register">Register</button>
    <button @click="Login">Login</button>
        </div>

    </body>
    
</template>

<script>

import homeimg from '../assets/HomePage.png'
export default{

    data(){

        return {image : homeimg}
    },

methods:
{
    Register(){
        this.$router.push('/register');
    },

    Login(){
        this.$router.push('/login');
    }
}
}
</script>

<style scoped>

* {
    
    margin:0px;
    padding:0px;
    box-sizing: border-box;

}

body{
    padding-top: 75px;
}

.middle{
    position: fixed;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	width: 400px;
	height: 350px;
	padding: 80px 40px;
	background: rgba(253, 253, 253, 0.7);
    align-items: center;
    justify-content: center;

}

.home-page::before{
    width: 100%;
	height: 100%;
	content: "";
	position: fixed;
	left: 0;
	right: 0;
	top: 0;
	bottom: 0;
	z-index: -1;
	display: block;
	filter: blur(2px);
    background-image: url('/static/car.jpeg');
	background-position: center center;
	background-repeat:no-repeat;
	background-attachment: fixed;
	-webkit-background-size: cover;
	background-size: cover;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}


.middle h2{
    margin: 0;
	padding: 0 0 20px;
	color: rgb(0, 0, 0);
	text-align: center;
	text-transform: uppercase;
}

.middle p {
    margin: 0;
	padding: 0;
	font-weight: bold;
	color: rgb(7, 0, 0);
    text-align: center;
}


#reg_btn{
    min-width:170px;
    align-self: center;
	margin-right: 0.5em;
}

#login_btn{
    min-width:170px;
}

.btns {
    display: flex;
    justify-content: center;
    padding-top: 20px;
}


</style>