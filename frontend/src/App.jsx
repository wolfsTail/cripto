import CardCryptoInstance from "./components/CardCryptoInstance.jsx"
import React, { useEffect } from 'react';
import { AppstoreOutlined } from '@ant-design/icons';
import { Menu } from 'antd';
import axios from 'axios';

const items = [
  {
    key: 'sub1',
    label: 'Криптовалюты',
    icon: <AppstoreOutlined/>,
    children: [
      {
        key: 'g1',
        label: 'Item 1',
        type: 'group',
      },
      {
        key: 'g2',
        label: 'Item 2',
        type: 'group',
      },
    ],
  },
];
const App = () => {

  const fetchData = () => {
    axios.get("http://127.0.0.1:8000/currencies/list/").then(response => {
      console.log(response);
    })
  };

  useEffect(() => {
    fetchData()
  }, []
    );

  const onClick = (e) => {
    console.log('click ', e);
  };
  return (
    <Menu
      onClick={onClick}
      style={{
        width: 256,
      }}
      defaultSelectedKeys={['1']}
      defaultOpenKeys={['sub1']}
      mode="inline"
      items={items}
    />
  );
};
export default App;