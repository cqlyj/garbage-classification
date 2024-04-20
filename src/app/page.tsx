import Link from "next/link";
import { ImageUpload } from "./components/image-upload";

export default function Home() {
  return (
    <div className="mt-16 min-w-[500px] ">
      <h1 className="font-bold text-5xl text-center text-slate-950">
        Upload your garbage image here!
      </h1>
      <div className="flex justify-evenly w-full mt-10">
        <ImageUpload />
      </div>
      <div className="flex justify-center items-center">
        <div className="mt-10 bg-slate-200 rounded-lg border w-1/2">
          <p className="text-3xl text-center">This is food garbage</p>
        </div>
      </div>
    </div>
  );
}
