document.addEventListener("DOMContentLoaded", function() {
    const loanAmount = document.getElementById("loanAmount");
    const interestRate = document.getElementById("interestRate");
    const tenure = document.getElementById("tenure");

    const loanAmountDisplay = document.getElementById("loanAmountDisplay");
    const interestRateDisplay = document.getElementById("interestRateDisplay");
    const tenureDisplay = document.getElementById("tenureDisplay");

    const emiAmount = document.getElementById("emiAmount");
    const totalInterest = document.getElementById("totalInterest");
    const totalPayment = document.getElementById("totalPayment");

    function calculateEMI() {
        let P = parseInt(loanAmount.value);
        let R = parseFloat(interestRate.value) / 12 / 100;
        let N = parseInt(tenure.value) * 12;

        let EMI = (P * R * Math.pow(1 + R, N)) / (Math.pow(1 + R, N) - 1);
        let totalPay = EMI * N;
        let totalInt = totalPay - P;

        emiAmount.innerText = EMI.toFixed(0);
        totalInterest.innerText = totalInt.toFixed(0);
        totalPayment.innerText = totalPay.toFixed(0);

        loanAmountDisplay.value = P.toLocaleString();
        interestRateDisplay.value = interestRate.value + "%";
        tenureDisplay.value = tenure.value + " Yr";
    }

    loanAmount.addEventListener("input", calculateEMI);
    interestRate.addEventListener("input", calculateEMI);
    tenure.addEventListener("input", calculateEMI);

    calculateEMI();
});












