## <font color="green">TI DM81xx hdvpss</font> ##

<p align="left">
[返回](/dm81xx/issue)
<p>
<hr />

*	[e2e.ti.com - tvp5147 capture error on emv8148 iocard using DVRRDK3.0](http://e2e.ti.com/support/dsp/davinci_digital_media_processors/f/716/t/249203.aspx)
<pre><code>

	for(vipInstId=0; vipInstId<1; vipInstId++)
	{
		pCaptureInstPrm = &capturePrm.vipInst[vipInstId];
		pCaptureInstPrm->vipInstId = SYSTEM_CAPTURE_INST_VIP1_PORTA;//(SYSTEM_CAPTURE_INST_VIP0_PORTA+vipInstId)%SYSTEM_CAPTURE_INST_MAX;
		pCaptureInstPrm->videoDecoderId = SYSTEM_DEVICE_VID_DEC_TVP5147_DRV;
		pCaptureInstPrm->inDataFormat = SYSTEM_DF_YUV422P;
		pCaptureInstPrm->standard = SYSTEM_STD_576I;
		pCaptureInstPrm->numOutput = 1;
		
		pCaptureOutPrm = &pCaptureInstPrm->outParams[0];
		pCaptureOutPrm->dataFormat = SYSTEM_DF_YUV422I_YUYV;
		pCaptureOutPrm->scEnable = FALSE;
		pCaptureOutPrm->scOutWidth = 0;
		pCaptureOutPrm->scOutHeight = 0;
		pCaptureOutPrm->outQueId = 0;
	}
	
	if (pInstPrm->videoDecoderId == FVID2_VPS_VID_DEC_TVP5147_DRV)
	{
		Vps_printf("pVipCreateArgs->videoIfMode = %d\n",pVipCreateArgs->videoIfMode);
		inScanFormat = FVID2_SF_INTERLACED;
	
		if(pObj->createArgs.enableSdCrop)
			pInst->maxWidth = 704;
		else
			pInst->maxWidth = 720;

		if (pObj->isPalMode)
			pInst->maxHeight = 288;
		else
			pInst->maxHeight = 240;

		inWidth = pInst->maxWidth;
		inHeight = pInst->maxHeight;

		pVipCreateArgs->videoIfMode = VPS_CAPT_VIDEO_IF_MODE_16BIT;

		pVipCreateArgs->numCh = 1;
		pVipCreateArgs->videoCaptureMode =
		VPS_CAPT_VIDEO_CAPTURE_MODE_SINGLE_CH_NON_MUX_DISCRETE_SYNC_ACTVID_VBLK;
	}
</code></pre>

<pre><code><font color="blue">
	I think TVP5147 supports 8bit interface so you should set:
		pVipCreateArgs->videoIfMode = VPS_CAPT_VIDEO_IF_MODE_8BIT;
	Video capture mode should be set to: 
		pVipCreateArgs->videoCaptureMode = VPS_CAPT_VIDEO_CAPTURE_MODE_SINGLE_CH_NON_MUX_EMBEDDED_SYNC;
	I use vin0 A to capture 8bit, It work ok!
</font></code></pre>

<hr />
<p align="right">
[返回](/dm81xx/issue)
<p>

