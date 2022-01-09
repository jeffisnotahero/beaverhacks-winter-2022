// Fetch and popualte actuals entry
async function populateActualsEntry(url){

    // Fetch data
    let response = await fetch(url)
    let data = await response.json()
    console.log("Actual Data", data)

    //  Populate both dropdown list
    let actualsEntry = data["data"]
    let dropdownList1 = document.getElementById("actuals-dropdown-list-1")
    let dropdownList2 = document.getElementById("actuals-dropdown-list-2")
    
    for (let i=0; i<actualsEntry.length; i++){

        let option = actualsEntry[i]

        // Actuals dropdown list 1
        let element1 = document.createElement("option");
        element1.textContent = option
        element1.value = option
        dropdownList1.appendChild(element1)

        // Actuals dropdown list 2
        let element2 = document.createElement("option");
        element2.textContent = option
        element2.value = option
        dropdownList2.appendChild(element2)
    }
}

// Fetch and populate state entry
async function populateStateEntry(url){

    // Fetch data
    let response = await fetch(url)
    let data = await response.json()
    console.log("State Data", data)

    // Populate state entry
    let state = data["data"]
    let dropdown_list = document.getElementById("state-dropdown-list")

    for (let i=0; i<state.length; i++){
        let option = state[i]
        let element = document.createElement("option");
        element.textContent = option
        element.value = option
        dropdown_list.appendChild(element)
    }
}

// Fetch and populate actuals entry data
async function getActualsEntryData(url, state, type, tag){

    // Fetch data /get_actuals_entry_data/<string:state>/actuals/<string:data>
    let response = await fetch(`${url}/${state}/actuals/${type}`)
    let data = await response.json()
    console.log("Actuals Entry Data", data)

    // Populate
    const value = data["data"]
    const span = document.getElementById(tag)
    span.textContent = value
}

// Generate random color
function dynamicColors() {
    var r = Math.floor(Math.random() * 255);
    var g = Math.floor(Math.random() * 255);
    var b = Math.floor(Math.random() * 255);
    return "rgba(" + r + "," + g + "," + b + ", 0.5)";
}

// Generate chart
function generateDoughnutChart(){

    document.getElementById("generate-graph-button").onclick = function(){

        // Get Amount
        actuals1 = document.getElementById("actuals-dropdown-list-amount-1")
        actuals2 = document.getElementById("actuals-dropdown-list-amount-2")
        console.log(actuals1.innerText)
        console.log(actuals2.innerText)

        // Get State name from drop list 
        var state_element = document.getElementById("state-dropdown-list");
        var state_value = state_element.options[state_element.selectedIndex].value;
        console.log(state_value)

        // Entry name from drop list 1
        var actuals_element = document.getElementById("actuals-dropdown-list-1");
        var actuals_value = actuals_element.options[actuals_element.selectedIndex].value;
        console.log(actuals_value)

        // Entry name from drop list 2
        var actuals_element1 = document.getElementById("actuals-dropdown-list-2");
        var actuals_value1 = actuals_element1.options[actuals_element1.selectedIndex].value;
        console.log(actuals_value1)

        // Generate Chart
        const data = {
            labels: [actuals_value, actuals_value1],
            datasets: [
                {
                label: 'Dataset 1',
                data: [actuals1.innerText, actuals2.innerText],
                backgroundColor: [
                    dynamicColors(),
                    dynamicColors(),
                ],
                }
            ]
            };
    
        const config = {
            type: 'doughnut',
            data: data,
            options: {
              responsive: true,
              plugins: {
                legend: {
                  position: 'top',
                },
                title: {
                  display: true,
                  text: state_value
                }
              }
            },
          };
        
        const myChart = new Chart(
            document.getElementById('myChart'),
            config
            );
        
        // Generate downloadable chart
        var image = myChart.toBase64Image();
        console.log(image);
        
        document.getElementById("download-graph-button").disabled = false;
        downloadElement = document.getElementById("download-link")
        downloadElement.href = myChart.toBase64Image();
        downloadElement.download = 'chart.png';
    }
}

// Clear chart
function clearDoughnutChart(){
    document.getElementById("clear-graph-button").onclick = function(){
        document.getElementById("download-graph-button").disabled = true
        document.getElementById("chart-div").innerHTML = '<canvas id="myChart"></canvas>'
    }
}

// Download Chart
function downloadDoughnutChart(){
    document.getElementById("download-graph-button").onclick = function(){
        element = document.getElementById("download-link")
        console.log("click")
        element.click()
    }
}

// Populate Actual dropdown list
function populateActualsEntryData(){

    // Ensure user chooses state first
    document.getElementById("actuals-dropdown-list-1").disabled = true;
    document.getElementById("actuals-dropdown-list-2").disabled = true;
    document.getElementById("state-dropdown-list").onchange = function(){
        document.getElementById("actuals-dropdown-list-1").disabled = false;
        document.getElementById("actuals-dropdown-list-2").disabled = false;
    }

    // Get data of Actuals dropdown list 1
    document.getElementById("actuals-dropdown-list-1").onchange = function(){

        var state_element = document.getElementById("state-dropdown-list");
        var state_value = state_element.options[state_element.selectedIndex].value;
        console.log(state_value)

        var actuals_element = document.getElementById("actuals-dropdown-list-1");
        var actuals_value = actuals_element.options[actuals_element.selectedIndex].value;
        console.log(actuals_value)

        getActualsEntryData("/get_actuals_entry_data", state_value, actuals_value, "actuals-dropdown-list-amount-1")
    }
    
    // Get data of Actuals dropdown list 2
    document.getElementById("actuals-dropdown-list-2").onchange = function(){

        var state_element = document.getElementById("state-dropdown-list");
        var state_value = state_element.options[state_element.selectedIndex].value;
        console.log(state_value)

        var actuals_element = document.getElementById("actuals-dropdown-list-2");
        var actuals_value = actuals_element.options[actuals_element.selectedIndex].value;
        console.log(actuals_value)

        getActualsEntryData("/get_actuals_entry_data", state_value, actuals_value, "actuals-dropdown-list-amount-2")
    }

}

// Main
document.addEventListener("DOMContentLoaded", function(){
    populateStateEntry("/get_state_entry/")
    populateActualsEntry("/get_actuals_entry/")
    populateActualsEntryData()

    generateDoughnutChart()
    clearDoughnutChart()
    downloadDoughnutChart()

})