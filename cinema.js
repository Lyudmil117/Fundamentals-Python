function cinema(input) {
    let movie = input[0];
    let row = Number(input[1]);
    let col = Number(input[2]);
    
    let price = 0;

    if (movie === "Premiere"){
        price =  12;
    } else if (movie === "Normal"){
        price = 7.5;
    } else if (movie === "Discount"){
        price = 5
    }

    let total = row * col * price;
    console.log(`${total.toFixed(2)} leva `)
}

cinema[("Normal", "5", "2")]