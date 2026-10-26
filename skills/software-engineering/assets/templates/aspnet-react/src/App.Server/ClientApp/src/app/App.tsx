import { Route, Routes } from 'react-router-dom';
export function App() {
  return <Routes><Route path="/" element={<main aria-label="Application" />} /><Route path="*" element={<main><h1>404</h1></main>} /></Routes>;
}
