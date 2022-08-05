window.testProcedureGenerate = function (form) {
    var usCore = form.usCore.value;
    var smartAppLaunch = form.smartAppLaunch.value;
    var bulkData = form.bulkData.value;

    var testProcedureFile = "";

    if ((usCore == "us-core-3.1.1") && (smartAppLaunch == "smart-app-launch-1.0.0") && (bulkData == "bulk-data-1.0.0")) {
        // Base Regulatory
        testProcedureFile = "../g10-test-procedures/OIv5O/";
    } else if ((usCore == "us-core-4.0.0") && (smartAppLaunch == "smart-app-launch-1.0.0") && (bulkData == "bulk-data-1.0.0")) {
        testProcedureFile = "../g10-test-procedures/svap-test-procedure-1/index.html";
    } else if ((usCore == "us-core-5.0.1") && (smartAppLaunch == "smart-app-launch-1.0.0") && (bulkData == "bulk-data-1.0.0")) {
        testProcedureFile = "../g10-test-procedures/svap-test-procedure-2/index.html";
    } else if ((usCore == "us-core-3.1.1") && (smartAppLaunch == "smart-app-launch-2.0.0") && (bulkData == "bulk-data-1.0.0")) {
        // SVAP option (US Core v3.1.1 + USCDI V1, SMART App Launch v2, Bulk Data v1)
        testProcedureFile = "../g10-test-procedures/caQqq";
    } else if ((usCore == "us-core-4.0.0") && (smartAppLaunch == "smart-app-launch-2.0.0") && (bulkData == "bulk-data-1.0.0")) {
        testProcedureFile = "../g10-test-procedures/svap-test-procedure-4/index.html";
    } else if ((usCore == "us-core-5.0.1") && (smartAppLaunch == "smart-app-launch-2.0.0") && (bulkData == "bulk-data-1.0.0")) {
        // SVAP option (US Core v5.0.1 + USCDI V2, SMART App Launch v2, Bulk Data v1)
        testProcedureFile = "../g10-test-procedures/jQuzj";
    } else if ((usCore == "us-core-3.1.1") && (smartAppLaunch == "smart-app-launch-1.0.0") && (bulkData == "bulk-data-2.0.0")) {
        testProcedureFile = "../g10-test-procedures/svap-test-procedure-6/index.html";
    } else if ((usCore == "us-core-4.0.0") && (smartAppLaunch == "smart-app-launch-1.0.0") && (bulkData == "bulk-data-2.0.0")) {
        testProcedureFile = "../g10-test-procedures/svap-test-procedure-7/index.html";
    } else if ((usCore == "us-core-5.0.1") && (smartAppLaunch == "smart-app-launch-1.0.0") && (bulkData == "bulk-data-2.0.0")) {
        testProcedureFile = "../g10-test-procedures/svap-test-procedure-8/index.html";
    } else if ((usCore == "us-core-3.1.1") && (smartAppLaunch == "smart-app-launch-2.0.0") && (bulkData == "bulk-data-2.0.0")) {
        testProcedureFile = "../g10-test-procedures/svap-test-procedure-9/index.html";
    } else if ((usCore == "us-core-4.0.0") && (smartAppLaunch == "smart-app-launch-2.0.0") && (bulkData == "bulk-data-2.0.0")) {
        testProcedureFile = "../g10-test-procedures/svap-test-procedure-10/index.html";
    } else if ((usCore == "us-core-5.0.1") && (smartAppLaunch == "smart-app-launch-2.0.0") && (bulkData == "bulk-data-2.0.0")) {
        testProcedureFile = "../g10-test-procedures/svap-test-procedure-11/index.html";
    }

    if (testProcedureFile !== "") {
        window.location.href = testProcedureFile;
    }
}