window.testProcedureGenerate = function (form) {
    var usCore = form.usCore.value;
    var smartAppLaunch = form.smartAppLaunch.value;
    var bulkData = form.bulkData.value;

    var testProcedureFile = "../g10-test-procedures/".concat(usCore, "_", smartAppLaunch, "_", bulkData, "/index.html");

    if (testProcedureFile !== "") {
        window.location.href = testProcedureFile;
    }
}