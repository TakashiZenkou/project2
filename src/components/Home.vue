<template>

    <body>
    <div class="leftside ">
        
        <div class="hometext ">
            <div class="homeheadings">
                <h2 id = "homeheadingstext"> Buy and Sell Cars Online </h2>
            </div>
            <div class="homesubtext">
                <p id = "subtext shadow"> United Auto Sales provides the fastest, easiest and most user friendly way to buy or sell cars online.
                    Find a Great Price on a Vehicle You Want.
                </p>
            </div>
    </div>
    <div class="homebuttons">
        <button type = "button" @click="Register" class = "btn btn-primary rbtn shadow">Register</button>
        <button type = "button" @click="Login" class = "btn btn-success lbtn shadow">Login</button>

    </div>
        </div>

    <div class="rightside">

        <img :src ="image">
        
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
    padding-top: 25px;
    display:flex
    
}

.leftside{

    margin-top: 200px;
    margin-left:170px;
    margin-right:50px;

    max-width: 50%;
    display: flex;
    flex-direction: column;
}
.rightside {

    max-width: 50%;
}

.homeheadings{

    width:70%;
    padding-bottom: 20px;

}

#homeheadingstext{

    font-size: 48px;
    font-weight: bold;
}

.homesubtext{

    width:74%;
}

#subtext{

    color: rgb(50, 50, 50);
}

.homebuttons{
    
    padding-top: 10px;
    margin-top: 10px;
    display: flex;
    align-items: center;
    gap:10px;    
}

.rbtn{

    padding:10px 45px 10px 45px;
    border-radius: 10px;
    

}

.lbtn{

    padding:10px 53.8px 10px 53.8px;
    border-radius: 10px;

}
</style>