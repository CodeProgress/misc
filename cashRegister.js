// Adapted from "Building a Cash Register" on Codecademy

function StaffMember(name, discountPercent){
    this.name = name;
    this.discountPercent = discountPercent;
    this.totalPurchases = 0;
}

var joe = new StaffMember("Joe", 5);
var sam = new StaffMember("Sam", 10);

var cashRegister = {
    total: 0,
    lastTransactionAmount: 0,
    add: function(itemCost){
        this.total += (itemCost || 0);
        this.lastTransactionAmount = itemCost;
    },
    scan: function(item, quantity){
        switch (item){
        case "eggs": this.add(0.98 * quantity); break;
        case "milk": this.add(1.23 * quantity); break;
        case "magazine": this.add(4.99 * quantity); break;
        case "chocolate": this.add(0.45 * quantity); break;
        }
        return true;
    },
    voidLastTransaction: function(){
        this.total -= this.lastTransactionAmount;
        this.lastTransactionAmount = 0;
    },
    applyStaffDiscount: function(employee){
        this.total -= this.total * (employee.discountPercent/100);
    },
    addToStaffTotal: function(employee){
        employee.totalPurchases += this.total;
    },
    resetRegister: function(employee){
        this.total = 0;
        this.lastTransactionAmount = 0;
    },
    printAndFinalize: function(){
        // Show the total bill, rounded to two decimal digits
        console.log('Your bill is '+ cashRegister.total.toFixed(2));
        // Reset for next patron
        this.resetRegister();
    }
};

cashRegister.scan('chocolate', 2);
cashRegister.scan('eggs', 1);
cashRegister.scan('milk', 1);
cashRegister.scan('magazine', 3);

cashRegister.voidLastTransaction();

cashRegister.applyStaffDiscount(sam);
cashRegister.addToStaffTotal(sam);

cashRegister.printAndFinalize();

//Check values
console.log(cashRegister.total, cashRegister.lastTransactionAmount);
console.log(sam.totalPurchases);


//Start new transaction
cashRegister.scan('chocolate', 3);
cashRegister.scan('eggs', 4);
cashRegister.scan('milk', 5);
cashRegister.scan('magazine', 2);

cashRegister.voidLastTransaction();

cashRegister.applyStaffDiscount(sam);
cashRegister.addToStaffTotal(sam);

cashRegister.printAndFinalize();


console.log(cashRegister.total, cashRegister.lastTransactionAmount);
console.log(sam.totalPurchases);

