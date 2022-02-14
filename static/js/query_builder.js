// jQuery(document).ready(function(){
//     getQueryFilters()
// });
function displayQueryDiv(){
    
        document.getElementById('users').style.display="none"
        document.getElementById("welcome-div").style.display="none"
        document.getElementById('query-builder').style.display="block"
        
        getQueryFilters()
  
}
function getQueryFilters(){
    //populating query builder select options
    return jQuery.ajax({
        url: apiUrl+"/company/filters",
        type: "GET",
        
        success: function(response){
            filters= response.responseData.value.companyFilters.value
            populateFilters(filters)
          
        },
        error: function (jqXHR, textStatus) {
          console.log("error")
        }
    });   
}
async function populateFilters(filters){
    for (var i = 0; i < filters.length; i++) {
      
        for (const [key, value] of Object.entries(filters[i])) {
           
            select_id="filter-"+key
            var select = document.getElementById(select_id);
           
            var options=value
            for(var elem = 0; elem < options.length; elem++) {
                var opt = options[elem];
                var el = document.createElement("option");
                el.textContent = opt;
                el.value = opt;
                select.appendChild(el);
            }
        }
        
    }
}

function getQueryResults(){
    //getting query count
    var industry= $("#filter-industry option:selected").text();
    var city= $("#filter-city option:selected").text();
    var state= $("#filter-state option:selected").text();
    var country= $("#filter-country option:selected").text();
    var year_founded= $("#filter-year_founded option:selected").text();
    var query_count=0
    return jQuery.ajax({
        url: apiUrl+"/query/count",
        type: "GET",
        data:{"industry":industry,"city":city,"state":state,"country":country,"year_founded":year_founded},
        success: function(response){
            query_count  = response.responseData.value.companyFilters.value
            document.getElementById('msgDiv').style.display="block"
         document.getElementById('query-result').innerHTML=query_count +'  records found for the query ! '
         
        },
        error: function (jqXHR, textStatus) {
          console.log("error")
        }
    });   

}
function clearFields(){
    $('select').prop('selectedIndex', 0);
}
