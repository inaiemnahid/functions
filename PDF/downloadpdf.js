(function() {
    // 1. Define helper functions
    function rescale(width, height, fitWidth, fitHeight) {
        let ratio = width / height;
        let fitRatio = fitWidth / fitHeight;
        if (ratio <= fitRatio) {
            return [width, width / fitRatio];
        } else {
            return [height * fitRatio, height];
        }
    }

    function imageToBase64(img) {
        let canvas = document.createElement("canvas");
        let context = canvas.getContext("2d");
        canvas.width = img.naturalWidth;
        canvas.height = img.naturalHeight;
        context.drawImage(img, 0, 0, img.naturalWidth, img.naturalHeight);
        return canvas.toDataURL("image/png", 1.0);
    }

    // 2. Create Trusted Types policy (only if enforced)
    const policy = window.trustedTypes?.createPolicy('allowJsPDF', {
        createScriptURL: (url) => url
    });

    // 3. Dynamically load jsPDF
    let pdfScript = document.createElement("script");
    pdfScript.src = policy 
        ? policy.createScriptURL("https://unpkg.com/jspdf@latest/dist/jspdf.umd.min.js")
        : "https://unpkg.com/jspdf@latest/dist/jspdf.umd.min.js";

    pdfScript.onload = function () {
        try {
            let jsPDF = window.jspdf.jsPDF;
            let pdf = new jsPDF();
            let pdfWidth = pdf.internal.pageSize.getWidth();
            let pdfHeight = pdf.internal.pageSize.getHeight();

            let elements = document.getElementsByTagName("img");
            for (let img of elements) {
                if (!/^blob:/.test(img.src)) continue;

                console.log("Adding image:", img.src);
                let imgData = imageToBase64(img);
                let [newWidth, newHeight] = rescale(pdfWidth, pdfHeight, img.naturalWidth, img.naturalHeight);

                pdf.addImage(imgData, "PNG", 0, 0, newWidth, newHeight);
                pdf.addPage();
            }

            // Remove last empty page
            pdf.deletePage(pdf.internal.getNumberOfPages());
            pdf.save("download.pdf");
        } catch (e) {
            console.error("Error while creating PDF:", e);
        }
    };

    document.body.appendChild(pdfScript);
})();
