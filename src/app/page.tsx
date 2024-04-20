import { ImageUpload } from "./components/image-upload";

export default function Home() {
  return (
    <div className="mt-16 min-w-[600px]">
      <h1 className="font-bold text-5xl text-center text-slate-950">
        Upload your garbage image here!
      </h1>
      <div className="justify-center w-full mt-10 items-center flex flex-col">
        <ImageUpload />
      </div>
    </div>
  );
}
