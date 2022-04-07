<template>
    <body>
        <div class="container-sm">
            <h2 class ="font-weight-bold">Add New Car</h2>
        <div class="card shadow p-3 mb-5">
            <form @submit.prevent="" enctype="multipart/form-data" id = "addCarform">
            <div class="row mb-3">
                <div class="col-6">
                    <label for = "Make" class = "form-label font-weight-bold ">Make </label>
                    <input type ="text" placeholder="Enter Make" name = "Make" class = "form-control">
                    </div>
                <div class="col-6">
                    <label for = "Model" class ="form-label font-weight-bold" >Model </label>
                    <input type ="text" placeholder="Enter Model" name = "Model" class = "form-control">
                </div>
            </div>
            <div class="row mb-3">
                <div class="col">
                    <label for = "Colour" class ="font-weight-bold form-label">Colour </label>
                    <input type ="text" placeholder="Enter Colour" name = "Colour" class = "form-control">
                </div>
                <div class="col">
                    <label for = "Year" class ="font-weight-bold form-label">Year </label>
                    <input type ="text" placeholder="Enter Year" name = "Year" class = "form-control"    >
                </div>
            </div>
           <div class="row mb-3">
               <div class="col">
                    <label for = "Price" class ="font-weight-bold form-label">Price </label>
                    <input type ="text" placeholder="Enter Price" name = "Price" class = "form-control">
                </div>
                <div class="col">
                    <label for = "CarType" class ="font-weight-bold form-label">Car Type </label>
                    <select name="CarType" class="form-select">
                        <option selected>SUV</option>
                        <option value="1">Coupe</option>
                        <option value="2">Sedan</option>
                        <option value="3">Hatchback</option>
                        <option value="4">Station Wagon</option>
                        <option value="5">Pickup Truck</option>
                        <option value="5">Truck</option>

                    </select>

                </div>
            </div>

            <div class="row mb-3">
                <div class="col-6">
                    <label for = "Transmission" class = "font-weight-bold form-label">Transmission </label>
                    <select name="Transmission" class="form-select">
                        <option selected>Automatic</option>
                        <option value="1">Manual</option>
                    </select>

                </div>
            </div>
            

            <label for = "Description" class = "font-weight-bold form-label" >Description </label>
            <textarea name = "Description" placeholder="Enter Description" class = "form-control mb-3"></textarea>

            <label for = "photo" class = "font-weight-bold" >Upload Photo</label>
            <input type ="file" name = "photo" class = "form-control">
    
            <br>

            <button class="btn btn-success btn-md" type = 'submit'>Save</button>

        </form>
        </div>
    </div>

                    </body>
</template>

<script>

</script>

<style scoped>


.container-sm{


    width:40%;
    box-shadow: 2px;
    background-color: rgb(226, 223, 223);

}

textarea{
    
    resize: none;
}

.card {
    margin-top:40px;
    padding:40px;
    border-radius: 15px;
    background-color: white;

}

h2{

    margin-top: 20px;
}

*{

    font-family: sans-serif;
}

.font-weight-bold{

    font-weight: bold;
}

body{
  padding-top: 75px;
}

</style>