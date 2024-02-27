# -*- coding: utf-8 -*-
#
# Copyright (c) 2024, Globex Corporation
# All rights reserved.
#
import pytest

from connect_ext.events import HighLoadEventsApplication


@pytest.mark.asyncio
async def test_handle_asset_suspend_request_processing(
    async_connect_client,
    async_client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = HighLoadEventsApplication(async_connect_client, logger, config)
    result = await ext.handle_asset_suspend_request_processing(request)
    assert result.status == 'success'


@pytest.mark.asyncio
async def test_handle_asset_cancel_request_processing(
    async_connect_client,
    async_client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = HighLoadEventsApplication(async_connect_client, logger, config)
    result = await ext.handle_asset_cancel_request_processing(request)
    assert result.status == 'success'


@pytest.mark.asyncio
async def test_handle_tier_account_update_request_processing(
    async_connect_client,
    async_client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = HighLoadEventsApplication(async_connect_client, logger, config)
    result = await ext.handle_tier_account_update_request_processing(request)
    assert result.status == 'success'


@pytest.mark.asyncio
async def test_handle_usage_file_request_processing(
    async_connect_client,
    async_client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = HighLoadEventsApplication(async_connect_client, logger, config)
    result = await ext.handle_usage_file_request_processing(request)
    assert result.status == 'success'


@pytest.mark.asyncio
async def test_handle_asset_purchase_request_processing(
    async_connect_client,
    async_client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = HighLoadEventsApplication(async_connect_client, logger, config)
    result = await ext.handle_asset_purchase_request_processing(request)
    assert result.status == 'success'


@pytest.mark.asyncio
async def test_handle_asset_adjustment_request_processing(
    async_connect_client,
    async_client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = HighLoadEventsApplication(async_connect_client, logger, config)
    result = await ext.handle_asset_adjustment_request_processing(request)
    assert result.status == 'success'


@pytest.mark.asyncio
async def test_handle_tier_config_setup_request_processing(
    async_connect_client,
    async_client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = HighLoadEventsApplication(async_connect_client, logger, config)
    result = await ext.handle_tier_config_setup_request_processing(request)
    assert result.status == 'success'


@pytest.mark.asyncio
async def test_handle_tier_config_adjustment_request_processing(
    async_connect_client,
    async_client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = HighLoadEventsApplication(async_connect_client, logger, config)
    result = await ext.handle_tier_config_adjustment_request_processing(request)
    assert result.status == 'success'


@pytest.mark.asyncio
async def test_handle_asset_change_request_processing(
    async_connect_client,
    async_client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = HighLoadEventsApplication(async_connect_client, logger, config)
    result = await ext.handle_asset_change_request_processing(request)
    assert result.status == 'success'


@pytest.mark.asyncio
async def test_handle_asset_resume_request_processing(
    async_connect_client,
    async_client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = HighLoadEventsApplication(async_connect_client, logger, config)
    result = await ext.handle_asset_resume_request_processing(request)
    assert result.status == 'success'


@pytest.mark.asyncio
async def test_handle_tier_config_change_request_processing(
    async_connect_client,
    async_client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = HighLoadEventsApplication(async_connect_client, logger, config)
    result = await ext.handle_tier_config_change_request_processing(request)
    assert result.status == 'success'


@pytest.mark.asyncio
async def test_handle_product_custom_event_processing(
    async_connect_client,
    async_client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = HighLoadEventsApplication(async_connect_client, logger, config)
    result = await ext.handle_product_custom_event_processing(request)
    assert result.status == 'success'
    assert result.body == request


@pytest.mark.asyncio
async def test_handle_tier_config_setup_request_validation(
    async_connect_client,
    async_client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = HighLoadEventsApplication(async_connect_client, logger, config)
    result = await ext.handle_tier_config_setup_request_validation(request)
    assert result.status == 'success'
    assert result.body == request


@pytest.mark.asyncio
async def test_handle_asset_change_request_validation(
    async_connect_client,
    async_client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = HighLoadEventsApplication(async_connect_client, logger, config)
    result = await ext.handle_asset_change_request_validation(request)
    assert result.status == 'success'
    assert result.body == request


@pytest.mark.asyncio
async def test_handle_product_action_execution(
    async_connect_client,
    async_client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = HighLoadEventsApplication(async_connect_client, logger, config)
    result = await ext.handle_product_action_execution(request)
    assert result.status == 'success'
    assert result.body == request


@pytest.mark.asyncio
async def test_handle_asset_purchase_request_validation(
    async_connect_client,
    async_client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = HighLoadEventsApplication(async_connect_client, logger, config)
    result = await ext.handle_asset_purchase_request_validation(request)
    assert result.status == 'success'
    assert result.body == request


@pytest.mark.asyncio
async def test_handle_tier_config_change_request_validation(
    async_connect_client,
    async_client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = HighLoadEventsApplication(async_connect_client, logger, config)
    result = await ext.handle_tier_config_change_request_validation(request)
    assert result.status == 'success'
    assert result.body == request
