class Car{
    constructor(color){
        this.color = color;
    }
    run(){};
}

let car = new Car("green");

let carProto = Object.getPrototypeOf(car);
console.log(carProto);
let objProto = Object.getPrototypeOf(carProto);
console.log(objProto);

