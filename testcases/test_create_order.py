from apexpro.http_private_sign import HttpPrivateSign
import os
import sys
import time
import pytest
import allure

root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-2])
sys.path.append(root_path)

from apexpro.constants import NETWORKID_TEST, APEX_OMNI_HTTP_TEST, NETWORKID_MAIN, APEX_OMNI_HTTP_MAIN

#
key = '589148de-2607-b4e8-afb1-b6bd736e99ba'
secret = 'COjM40p9Un3BqonWIBbdWrzwAMP_oH9GI1F0lqQz'
passphrase = 'JpGZl9csREhoRqP8efHR'

seeds = '0xdb0ada5cd8dc1c8bea71c801bbace172c67f25488d0e8ca4fd9e6341092254a325e4dc676e557d5fb6f853b50b3877c613457f60167121a17f31562cbdad7f4d1b'
l2Key = '0xcdfe7b8db0d7ed15db2b94f0ebff6e0ddf4df2a48e2de6a703d80845996cac21'


@allure.epic("订单管理")
@allure.feature("订单创建")
class TestOrder:
    
    @allure.story("创建市价买单")
    @allure.title("创建SOL-USDT市价买单")
    @pytest.mark.order
    def test_create_market_buy_order(self, api_client):
        """测试创建市价买单"""
        with allure.step("获取配置信息"):
            configs = api_client.configs_v3()
            
        with allure.step("获取账户信息"):
            account_data = api_client.get_account_v3()
            api_client.accountV3 = account_data
            
        with allure.step("创建市价买单"):
            current_time = time.time()
            create_order_res = api_client.create_order_v3(
                symbol="SOL-USDT",
                side="BUY",
                type="MARKET",
                size="1.2",
                timestampSeconds=current_time,
                price="126",
                brokerId=6443
            )
            
        with allure.step("验证订单创建结果"):
            assert create_order_res is not None, "订单创建失败"
            allure.attach(str(create_order_res), "订单响应", allure.attachment_type.TEXT)
            
    @allure.story("创建限价卖单")
    @allure.title("创建SOL-USDT限价卖单")
    @pytest.mark.order
    def test_create_limit_sell_order(self, api_client):
        """测试创建限价卖单"""
        with allure.step("获取配置信息"):
            configs = api_client.configs_v3()
            
        with allure.step("获取账户信息"):
            account_data = api_client.get_account_v3()
            api_client.accountV3 = account_data
            
        with allure.step("创建限价卖单"):
            current_time = time.time()
            create_order_res = api_client.create_order_v3(
                symbol="SOL-USDT",
                side="SELL",
                type="LIMIT",
                size="1.2",
                timestampSeconds=current_time,
                price="130",
                brokerId=6443
            )
            
        with allure.step("验证订单创建结果"):
            assert create_order_res is not None, "订单创建失败"
            allure.attach(str(create_order_res), "订单响应", allure.attachment_type.TEXT)
