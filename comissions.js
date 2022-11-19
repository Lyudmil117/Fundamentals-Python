function comission(input){
    let city = input[0];
    let salesVolume = Number(input[1]);
    let bonus = 0

    if ((city != "Sofia" && city != "Plovdiv" && city != "Varna") || salesVolume < 0){
        console.log("error")
    
    } else if (city === "Sofia"){
        if (0 <= salesVolume && salesVolume <= 500){
            bonus = 0.05 
        } else if ( 500 < salesVolume && salesVolume <= 1000){
            bonus = 0.07 
        } else if (1000 < salesVolume && salesVolume <= 10000) {
            bonus = 0.08 
        } else if (10000 < salesVolume) {
            bonus = 0.12 
        }
        console.log(`${(bonus * salesVolume).toFixed(2)}`)
    }

     else if (city === "Varna"){
        if (0 <= salesVolume && salesVolume <= 500){
            bonus = 0.045 
        } else if ( 500 < salesVolume && salesVolume <= 1000){
            bonus = 0.075 
        } else if (1000 < salesVolume && salesVolume <= 10000) {
            bonus =  0.1 
        } else if (10000 < salesVolume) {
            bonus = 0.13 
        }
        console.log(`${(bonus * salesVolume).toFixed(2)}`) 

    } else if (city === "Plovdiv"){
        if (0 <= salesVolume && salesVolume <= 500){
            bonus = 0.055 
        } else if ( 500 < salesVolume && salesVolume <= 1000){
            bonus = 0.08 
        } else if (1000 < salesVolume && salesVolume <= 10000) {
            bonus = 0.12 
        } else if (10000 < salesVolume) {
            bonus = 0.145
        }
        console.log(`${(bonus * salesVolume).toFixed(2)}`)
    } 
        

}
comission(["Sofia", "1500"])