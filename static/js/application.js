
var apiUrl= 'http://127.0.0.1:8000'


function displayUserdiv(){
    document.getElementById('query-builder').style.display="none"
    document.getElementById("welcome-div").style.display="none"
    document.getElementById('users').style.display="block"
  
    getUsers()
    
}
function displayHomediv(){
    document.getElementById('query-builder').style.display="none"
    document.getElementById("welcome-div").style.display="block"
    document.getElementById('users').style.display="none"
}
function getUsers(){
    return jQuery.ajax({
        url: apiUrl+"/user/details",
        type: "GET",
        success: function(response){
          userData= response.responseData.value.user_data.value
          GenerateTable(userData)
          
        },
        error: function (jqXHR, textStatus) {
          console.log("error")
        }
    });   
  }
  function GenerateTable(userData) {
  
    
    //Create a HTML Table element.
    var table = document.createElement("TABLE");
    table.border = "1";
    table.className="table table-striped table-hover"
    //Get the table headers.
    var columnCount = ["Name","Email","Phone"]

    //Add the header row.
    var row = table.insertRow(-1);
    for (var i = 0; i < columnCount.length; i++) {
        var headerCell = document.createElement("TH");
        headerCell.innerHTML = columnCount[i];
        row.appendChild(headerCell);
    }
   
    for (var i = 0; i < userData.length; i++) {
        
        row = table.insertRow(-1);
        
        let name = row.insertCell(0);
       
        name.innerHTML = userData[i]['fields']['username'];
        let email=row.insertCell(1);
        email.innerHTML = userData[i]['fields']['email'];
        let phone=row.insertCell(2);
        phone.innerHTML=userData[i]['fields']["phone"]
    }

   
    var dvTable = document.getElementById("user-data");
    dvTable.innerHTML = "";
    dvTable.appendChild(table);
}