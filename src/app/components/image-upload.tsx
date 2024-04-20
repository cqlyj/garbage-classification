"use client";

import { UploadDropzone } from "@/utils/uploadthing";
import Image from "next/image";
import { useState } from "react";

export const ImageUpload = () => {
  const [imageURL, setImageURL] = useState<string>("");

  return (
    <div>
      <UploadDropzone
        endpoint="strictImageAttachment"
        onClientUploadComplete={(res) => {
          console.log("Files: ", res);
          setImageURL(res[0].url);
        }}
        onUploadError={(error: Error) => {
          alert(`ERROR! ${error.message}`);
        }}
      ></UploadDropzone>
      {imageURL.length ? (
        <div>
          <Image src={imageURL} alt="image" width={500} height={300}></Image>
        </div>
      ) : null}
    </div>
  );
};
