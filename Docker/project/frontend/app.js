import express from "express";
import dotenv from "dotenv";
import { GetData } from "./data.js";
dotenv.config();

const app = express();

app.use(express.static("public"));

const URL = process.env.API_URL;

GetData(URL);

app.get("/get-data", async (req, res) => {
    try {
        const data = await GetData(URL);
        return res.status(200).json({
            success: true,
            message: "Data fetched successfully",
            data
        });
    }
    catch (error) {
        return res.status(500).json({
            message: "Error fetching data",
            error: error.message
        });
    }
});

app.listen(3000, () => {
    console.log("Server started on port 3000");
});