import './App.css';
import Excel from './components/Excel';

function App() {

  const headers = localStorage.getItem( 'headers' );
  const data = localStorage.getItem( 'data' );

  if (!headers) {
    headers = ['Title', 'Year', 'Rating', 'Comments'];
    data = [['Red Whine', '2021', '3', 'meh']];
  }
  return (
    <div>
      <Excel
        headers={['Name', 'Year']}
        initialData={[
          ['Charles', '1859'],
          ['Antoine', '1943'],
        ]}
        />
    </div>
  );
}
export default App;