# !/usr/bin/env python3
"""
测试缓存装饰器的asyncio修复
"""

from __future__ import annotations

import asyncio
import time

from xtwraps import cache_wrapper


# 测试同步函数缓存
@cache_wrapper(maxsize=5, ttl=2)
def sync_function(x: int) -> int:
    """同步测试函数"""
    print(f'执行同步函数: {x}')
    time.sleep(0.1)
    return x * 2


# 测试异步函数缓存
@cache_wrapper(maxsize=5, ttl=2)
async def async_function(x: int) -> int:
    """异步测试函数"""
    print(f'执行异步函数: {x}')
    await asyncio.sleep(0.1)
    return x * 3


async def test_async_cache():
    """测试异步缓存"""
    print('测试异步缓存...')

    # 第一次调用
    result1 = await async_function(5)
    print(f'第一次结果: {result1}')

    # 第二次调用（应该从缓存获取）
    result2 = await async_function(5)
    print(f'第二次结果: {result2}')

    # 不同参数
    result3 = await async_function(10)
    print(f'不同参数结果: {result3}')


def test_sync_cache():
    """测试同步缓存"""
    print('测试同步缓存...')

    # 第一次调用
    result1 = sync_function(3)
    print(f'第一次结果: {result1}')

    # 第二次调用（应该从缓存获取）
    result2 = sync_function(3)
    print(f'第二次结果: {result2}')

    # 不同参数
    result3 = sync_function(7)
    print(f'不同参数结果: {result3}')


def main():
    """主测试函数"""
    print('=== 测试缓存装饰器asyncio修复 ===')

    # 测试同步缓存
    test_sync_cache()

    print('\n' + '=' * 50 + '\n')

    # 测试异步缓存
    asyncio.run(test_async_cache())

    print('\n=== 测试完成 ===')


if __name__ == '__main__':
    main()
