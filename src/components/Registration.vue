<template>

    <div class="container">
        
        <form enctype="multipart/form-data">

            <label for = "username" >Username </label>
            <input type ="text" placeholder="Enter username" name = "username">

            <label for = "password" >Password </label>
            <input type ="text" placeholder="Enter password" name = "password">

            <label for = "fullname" >Fullname </label>
            <input type ="text" placeholder="Enter fullname" name = "fullname">

            <label for = "location" >Location </label>
            <input type ="text" placeholder="Enter fullname" name = "location">
            
            <label for = "bio" >Biography </label>
            <textarea name = "bio" ></textarea>

            <label for = "photo" >photo </label>
            <input type ="file" name = "photo">

            <br>

            <button class="btn-primary" type = 'submit'>Submit</button>

        </form>
    </div>

</template>

<script>

</script>

<style>

</style>