const { Storage } = require('@google-cloud/storage');
const path = require('path');

// Créer une instance du client Cloud Storage
const storage = new Storage();

// Chemins des fichiers locaux
const localFilePaths = ["E:/10_1.webp", "E:/11_1.webp"];

// Nom des fichiers dans le bucket
const blobNames = ["10_1.webp", "11_1.webp"];

// Nom du bucket
const bucketName = "abdelwahab-jemla-com.appspot.com";

// Référence au bucket Cloud Storage
const bucket = storage.bucket(bucketName);

// Uploader les fichiers dans le bucket
Promise.all(localFilePaths.map(async (localFilePath, index) => {
    const blobName = path.join("Images", blobNames[index]);
    const file = bucket.file(blobName);

    await bucket.upload(localFilePath, {
        destination: blobName
    });

    console.log(`Le fichier ${localFilePath} a été importé dans ${blobName}.`);
})).then(() => {
    console.log("Importation des fichiers terminée.");
}).catch(error => {
    console.error("Erreur lors de l'importation des fichiers :", error);
});
