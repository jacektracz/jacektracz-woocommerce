/*-----------------------------------------------------*- Mode: C++ -*-*/
/*    .../KNCB_CreditLimit.cpp ...                                     */
/*                                                                     */
/*    Author      :                                                    */
/*    Creation    :                                                    */
/*    Last change :  Sun Feb 19 03:17:38 2012  (antmenag)              */
/*                                                                     */
/*---------------------------------------------------------------------*/

/*---------------------------------------------------------------------*/
/*    include ...                                                      */
/*---------------------------------------------------------------------*/
#include <sstream>


#include <std/time.h>
#include <PS/ptime.h>

#include <KNETCommon/KNC_ConvId.h>
#include <KGLBase/KGLB_Date.h>


#include <KNETData/KNET_EnquiryHeaderChange.h> //pour enum RiskChoice...
#include <KNETData/KNET_LimitCoverageElement.h> //pour enum CreditKind...
#include <KNETData/KNET_Identity.h>
#include <KNETData/KGL_ReviewDateMessage.h>
#include <KNETData/KNET_LimitUseCurves.h>
#include <KNETData/KGL_ReviewDate.h>

#include <KNETService/KNET_TaskStatus.h>
#include <KNETService/KNET_ComputeResponse.h>
#include <KNETService/KNET_DataResponse.h>
#include <KNETService/KNET_DoubleValidationResponse.h>

#include "KNCBToolkit/KNCBTK_Identity.h" //for KNCBTK_IdentityTool
#include "KGLDbCommon/KGLDB_WhereClause.h"

#include <business/Cpty.h>
#include <business/CreditLimit.h>
#include <business/Industry.h>
#include <business/Instrument.h>
#include <business/Country.h>
#include <business/RiskWeightCoverage.h>
#include <business/Rating.h>
#include <business/RatingAgency.h>
#include <business/Currency.h>
#include <business/Folder.h>
#include <business/KNUser.h>
#include <business/CreditLimitCoverage.h>
#include <business/TimeBand.h>
#include <business/RatingAlias.h>
#include <business/CptyAlias.h>
#include <business/RatingAlias.h>
#include <business/RatingAgencyAlias.h>
#include <business/IndustryAlias.h>
#include <business/InstrumentAlias.h>
#include <business/CountryAlias.h>
#include <business/CurrencyAlias.h>
#include <business/FolderAlias.h>
#include <business/KNUserAlias.h>
#include <business/FolderLink.h>
#include <business/CptyLink.h>
#include <business/FolderLink.h>
#include <business/CountryLink.h>
#include <business/IndustryLink.h>
#include <business/InstrumentLink.h>
#include <business/CurrencyLink.h>
#include <business/KNUserLink.h>
#include <business/AccessDefaultKNUser.h>
#include <business/TimeBand.h>
#include <business/CreditReservationDeal.h>
#include <business/Source.h>
#include <business/DealTable.h>
#include <business/DealTableAlias.h>
#include <business/RatingLink.h>
#include <business/CLMasterDVInsert.h>
#include <business/CreditTBAllocSchedElt.h>
#include <business/TimeBandCoverageElt.h>
#include <business/TimeBandAlias.h>
#include <business/DealNumber.h>
#include <business/LimitNumber.h>
#include <business/KNUserConfig.h>
#include <business/DealLog.h>
#include <business/Source.h>
#include <business/Delta.h>
#include <business/DeltaStamp.h>
#include <business/CreditLimitLog.h>
#include <business/CreditLimitDelta.h>
#include <business/KGRProject.h>
#include <business/KPfeCurveAssignmentSetup.h>
#include <business/CreditCoverageMC.h>

#include <KGLDbCommon/KNSDBC_DBConnection.h>

#include <KNETDBChoices/KNDBC_Choices.h>

#include <KNETDBTools/KDBT_DBEnv.h>


#include <KGRKTools/KT_PtrWrapper.h>


/* C++ */
#include <assert.h>
#include <KGLCommon/KGL_Util.h>
#include <KGLData/KGL_CreditReservationTransferAdapterVectorImpl.h>
#include <KGLData/KGL_CreditReservationTransferAdapterImpl.h>


#include <KNETService/KNET_CreditLimitResponse.h>
#include <KNETService/KGL_DataResponse.h>
#include <KNETService/KGL_DataCollResponse.h>
#include <KNETService/KGL_Response.h>
#include <KNETCommon/KNC_Date.h>


#include <KNDB_Tools.h>
#include <KNDB_Mutex.h>

#ifdef WINNT
#include <windows.h>
#else
#include <unistd.h>
#endif
#include <KNETFin/KF_Pair.h>

#include "KNCB_CreditLimit.h"
#include "KNCB_CreditLimitDashboardsDataFetcher.h"
#include <KNETDashboardCallbacks/KNCB_Calendar.h>

#include <KGLEnums/KGLE_AsyncMsgType.h>
#include <KNETCoreCompute/KNC_ConvChoice.h>
#define INFINIT_TB_SHORTNAME "0D-+"

#define LIMIT_IS_SOURCE_OF_ALLOCATION_TRANSFER "The limit is a source of allocation transfer \n=> cancel the transfer before deleting the source limit!"



/*---------------------------------------------------------------------*/
/*    type ...                                                         */
/*---------------------------------------------------------------------*/


typedef KNDB_Link<CptyLink_var, Cpty_var>::Collection CptyLinkCollection;
typedef KNDB_Link<CountryLink_var, Country_var>::Collection CountryLinkCollection;
typedef KNDB_Link<FolderLink_var, Folder_var>::Collection FolderLinkCollection;
typedef KNDB_Link<IndustryLink_var, Industry_var>::Collection IndustryLinkCollection;
typedef KNDB_Link<InstrumentLink_var, Instrument_var>::Collection InstrumentLinkCollection;
typedef KNDB_Link<CurrencyLink_var, Currency_var>::Collection CurrencyLinkCollection;
typedef KNDB_Link<KNUserLink_var, KNUser_var>::Collection KNUserLinkCollection;
typedef KNDB_Link<RatingLink_var, Rating_var>::Collection RatingLinkCollection;


/*---------------------------------------------------------------------*/
/*    static ...                                                       */
/*---------------------------------------------------------------------*/

/*---------------------------------------------------------------------*/
/*    implementation ...                                               */
/*---------------------------------------------------------------------*/


KNCB_CreditLimit::KNCB_CreditLimit(KNC_ServerParams const& serverParams) :
    KNCBTK_ValidableData< KNCB_CreditLimit,
    KNET_CreditLimitChange,
    KNET_CreditLimitAccess,
    CreditLimitMaster_Factory,
    CreditLimitMaster_var,
    KNET_CreditLimitResponse,
    CLMasterToCheck_var,
    CLMasterToCheck_Factory,
    CLMasterDVInsert_var,
    CLMasterDVCoverage_var,
    CLMasterDVCoverage_Factory,
    CreditLimitMasterBase_var,
    KGL_CreditLimitAdapterVectorImpl,
	KGL_CreditLimitAdapterImpl,
    KGLE_AsyncMsgType::DV_LIMIT>( serverParams ),
    serverParams_                                    ( serverParams ),
    kncbtkCreditLimitNamedData_                      ( this ),
    kncbtkCreditLimitLimit_                          ( this ),
    kncbtkCreditLimitMasterLink_                         ( this ),
	kncbtkCreditLimitAccess_                         ( this )

{
    	kntcAudit_ = new KNTC_AuditSimple();
}


KNCB_CreditLimit::~KNCB_CreditLimit()
{
	delete kntcAudit_;
}


/*===================================================================================
  !! SPECIFIC !!
  ===================================================================================*/


void KNCB_CreditLimit::onGetReviewDateMessages( KNET_RequestHandle handle )
{
	static const char* fctName = " KNCB_CreditLimit::onGetReviewDateMessages";
	KH_DBG::dbg("KNCB_CreditLimit::onGetReviewDateMessages::method_start");
	KGLDB_WhereClause whereClause;
	CreditLimitMaster_var CLMaster;
	ReviewCredElt_var reviewCredElt;


	KNDB_LOOP_ONCE_BEGIN

		try
		{
			//ReviewerId =KNUserId OR EXISTS (SELECT 1 FROM LinkedKNUser WHERE KNUserIdParent = ReviewerId AND KNUserIdChild = KNUserId)
			string clause;
			whereClause.addCondition( " ReviewerId", "=", handle->getUser() );
			clause = whereClause.getConditions();
			whereClause.erase();
			whereClause.addCondition( " KNUserIdChild", "=", handle->getUser() );

			clause.append("  OR EXISTS (SELECT 1 FROM LinkedKNUser WHERE KNUserIdParent = CreditLimitMaster.ReviewerId AND ");
			clause.append(whereClause.getConditions());
			clause.append(")");

			CreditLimitMaster_Cltn_var psCreditLimitMasterColl = CreditLimitMaster_Factory::instance()->querySQLWhere(clause.c_str());

			KNC_Date today(KNC_ConvDate::getNow()) ;

			KGR_Date knettoday ;
			knettoday.setDate(today);

			KGR_Collection<KGL_ReviewDateMessage> reviewMessageColl;

			if(!PS_is_nil(psCreditLimitMasterColl) )
			{
				unsigned long collSize = psCreditLimitMasterColl->length() ;
				for (unsigned long i=0; i<collSize; ++i)
				{
					CLMaster = psCreditLimitMasterColl[ i ];

					//conversion date persitence KNC_Date
					KNC_Date date ;
					date.strToDate(CLMaster->NextReviewDate());

					if(date1lesseq2(date,today))  // la nextReviewDate est aujourdhui ou est passee ?
					{
						//ajout a la collection du message
						whereClause.erase();

						//tous les messages compris entre la derniere revue de message sur les limite et aujourdhui
						whereClause.addCondition( "CreditLimitMasterId", "=", CLMaster->Id() );
						whereClause.addCondition( "ReviewDate", ">", CLMaster->LastReviewDate() );
						whereClause.addCondition( "ReviewDate", "<=", KNET_DateToPS(knettoday).c_str() );

						//tous les messages compris entre la derniere date de review et aujourdhui.
						//whereClause.addCondition("ReviewDate", ">=", CLMaster->NextReviewDate());
						ReviewCredElt_Cltn_var psReviewDateColl = ReviewCredElt_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());

						//on n'affiche qu'un seul message...mais doit afficher une collection de message.
						if(!PS_is_nil(psReviewDateColl))
						{
							unsigned long collSize = psReviewDateColl->length();
							for (unsigned long i=0; i<collSize; ++i)
							{
								reviewCredElt = psReviewDateColl[i];

								KGL_ReviewDateMessage reviewMessageData(PSToKGR_Date(reviewCredElt->ReviewDate()),
																		PSToKNETLimitKind(CLMaster->LimitKind()) ,
																		CLMaster->ShortName(),
																		reviewCredElt->Msg() );

								reviewMessageColl.push_back(reviewMessageData);
							}
						}
					}
				}

				KNC_Result res=KGL_DataCollResponse<KGL_ReviewDateMessage>::sendSuccess(reviewMessageColl,reviewMessageColl.size(),handle);
				if(!res)
				{
					throw_LOGICAL(res.text());
				};
			}
		}
	catch (const PS_UserError& e)
	{
	  ERROR_LOG << e.description() << std::endl ;

		cerr << fctName << " usererror : " << e.description() << endl;
	  KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM,
								e.description(), handle);
		return;
	}
	catch (const PS_ServerError& e)
	{
		KNC_Result kncResultHE
			= KNDB_HANDLE_EXCEPTION(e);
		if (!kncResultHE)
		{
			ERROR_LOG << e.description << std::endl ;

			cerr <<  fctName << " pserror : " << e.description.buff() << endl;
			KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM,
									  e.description.buff(), handle);
			return;
		}
	}
	KNDB_LOOP_END
	KH_DBG::dbg("KNCB_CreditLimit::onGetReviewDateMessages::method_end");
}


/*
* onInsertReservation (KNET_Id...)		!! CreditLimit specific !!
* ???CREATE???
* ???INSERT???
*/
void
KNCB_CreditLimit::onInsertReservation (KGR_Id const& creditLimitMasterId,
                                       KGR_Id const* tbId,
                                       KNET_CreditReservationChange const& creditReservation,
                                       KNET_RequestHandle handle)
{
	static const char* fctName = "KNCB_CreditLimit::onInsertReservation";
	KH_DBG::dbg("KNCB_CreditLimit::onInsertReservation::insert");
	CreditLimit_var psCreditLimit;
	CreditLimitMaster_var psCreditLimitMaster;
	TimeBand_var psTB;
	TimeBandCoverageElt_var TBElement;

	//
	try
    {
		if ( !tbId || !strlen(tbId->getValue()))
			psTB = TimeBand_Factory::instance()->queryShortName(string(INFINIT_TB_SHORTNAME).c_str());
		else
			psTB = KNCBTK_CoreBasic<TimeBand_var, TimeBand_Factory>::queryId(*tbId);

		PS_Oid_var userOid(new PS_Oid);
		userOid->setOidVal((const unsigned char*)(handle->getUser()).getValue());
		psCreditLimitMaster = KNCBTK_CoreBasic<CreditLimitMaster_var
			,CreditLimitMaster_Factory>
			::queryId(creditLimitMasterId);

		if (PS_is_nil(psCreditLimitMaster))
        {
			string errMsg(CreditLimitMaster_Factory::instance()->className());
			errMsg+="Not Found ";
			//KNET_CreditLimitResponse::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
			KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
			return;
        }




		if (PS_is_nil(psTB))
        {
			string errMsg(TimeBand_Factory::instance()->className());
			errMsg+="Not Found ";
			//KNET_CreditLimitResponse::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
			KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
			return;
        }


		if(!CreditLimitMaster_Factory::instance()->hasAccess(false,true,psCreditLimitMaster,userOid))
        {
			throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }
		if(!PS_is_nil(psCreditLimitMaster->arcCptyCoverage()) &&
		   !Cpty_Factory::instance()->hasAccess(2,false,true,psCreditLimitMaster->arcCptyCoverage(),userOid))
        {
			throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }
		if(!PS_is_nil(psCreditLimitMaster->arcFolderCoverage()) &&
		   !Folder_Factory::instance()->hasAccess(2,false,true,psCreditLimitMaster->arcFolderCoverage(),userOid))
        {
			throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }
		//psCreditLimitMaster = CreditLimitMaster_Factory::instance()->queryKey(*psCreditLimit->CreditLimitMasterId(),PS_Defs::k_cacheThenDatabase) ;


		// NO NEED TO TBElement anymore, CreditLimit contains the AllocatedAmount for that TimeBand
		// TBElement = TimeBandCoverageElt_Factory::instance()->queryKey(*psCreditLimitMaster->Id(),*psTB->Id(), PS_Defs::k_cacheThenDatabase) ;


		// in order to keep the model safe, we get the CreditLimit_var which correspond to the right TB element
		//	psCreditLimit= CreditLimit_Factory::instance()->queryKey(*psCreditLimitMaster->Id(),*psTB->Id(), PS_Defs::k_cacheThenDatabase) ;

		KGLDB_WhereClause whereClause;
		whereClause.addCondition( "CreditLimitMasterId", "=", KGR_Id(psCreditLimitMaster->Id()->getOidVal()) );
		whereClause.addCondition( "TimeBandId", "=", KGR_Id(psTB->Id()->getOidVal()) );

		CreditLimit_Cltn_var CLCltn = CreditLimit_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());
		if(!PS_is_nil(CLCltn) && 0 != CLCltn->length() )
		{
			psCreditLimit = CLCltn[ 0ul ];
		}
		else
		{
			throw_NOTFOUND(CreditLimit_Factory::instance()->className());
		}

    }
	catch (const PS_UserError& e)
    {
		ERROR_LOG << e.description() << std::endl ;
		this->failure(e, handle);
		return;
    }
	catch (const PS_ServerError& e)
    {
		this->failure(e, handle);
		return;
    }
	try
    {
		if (!hasTableAccess(INS
							,CreditReservation_Factory::instance()->className()
							,handle->getUser()))
			return;
		//
    }
	catch (const PS_UserError& e)
    {
		
		WARNING_LOG << e.description()<< std::endl;
		KGL_Response::sendFailure(KNC_FailureCategory::SECURITY, e.description(), handle);
		return;
    }
	catch (const PS_ServerError& e)
    {
		ERROR_LOG << fctName <<": caught exception PS_ServerError, nm=" << (const char*)(e.name);
		ERROR_LOG << ", descr=" << (const char*)(e.description) << ", excpNm" << (const char*)(e.exceptionName()) << endl;
		KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
		return;
    }
	KNDB_LOOP_BEGIN
		try
		{
			//
			KNDB_T_WRITE


				if (!(psCreditLimitMaster->LimitKind().buff()[0]=='S'))
				{
					KNDB_T_ROLLBACK
						string errMsg(CreditLimitMaster_Factory::instance()->className());
					errMsg+=" wrong limit kind";
					KGL_Response::sendFailure(KNC_FailureCategory::LOGICAL, errMsg.c_str(), handle);
					return;
				}


			PS_Oid_var officeOid;
			PS_Oid_var userOid(new PS_Oid);
			userOid->setOidVal((const unsigned char*)(handle->getUser()).getValue());
			bool status=KNETUserIdToPSOfficeId(handle->getUser(), officeOid);




			if(status && !CreditLimitMaster_Factory::instance()->hasAccess(false,true,psCreditLimitMaster,userOid))
			{
				throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
			}
			if(status && !PS_is_nil(psCreditLimitMaster->arcCptyCoverage()) &&
			   !Cpty_Factory::instance()->hasAccess(2,false,true,psCreditLimitMaster->arcCptyCoverage(),userOid))
			{
				throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
			}
			if(status && !PS_is_nil(psCreditLimitMaster->arcFolderCoverage()) &&
			   !Folder_Factory::instance()->hasAccess(2,false,true,psCreditLimitMaster->arcFolderCoverage(),userOid))
			{
				throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
			}


			if(psCreditLimit->AllocatedAmount() <creditReservation.getAllocatedAmount())
			{
				KNDB_T_ROLLBACK
					string errMsg(CreditLimit_Factory::instance()->className());
				errMsg+=" reservation amount larger than the limit";
				KGL_Response::sendFailure(KNC_FailureCategory::LOGICAL, errMsg.c_str(), handle);
				return;
			}

			//////////////////////////////////////////////////////////////
			// cpty
			if (!psCreditLimitMaster->CptyId_CoverageNULL())
			{
				if(!creditReservation.isCptyCoverageNULL())
				{
					KGR_Id knetId;
					if	(!KNCBTK_Identifier<CptyAlias_var
						 ,CptyAlias_Factory>
						 ::KNET_IdentifierToId(&creditReservation.getCptyCoverage()
											   ,handle->getSource()
											   ,knetId)
						)
					{
						;
					}
					Cpty_var psCpty = KNCBTK_CoreBasic<Cpty_var
						,Cpty_Factory>::queryId(knetId);
					if (PS_is_nil(psCpty))
					{
						KNDB_T_ROLLBACK
							string errMsg(Cpty_Factory::instance()->className());
						errMsg+=" not found";
						KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
						return;
					}

					if(psCreditLimitMaster->arcCptyCoverage() ==psCpty)
					{
					}
					else
					{
						unsigned long i;

						CptyLinkCollection children;
						CptyLink_Factory::instance()->queryChildren(psCreditLimitMaster->arcCptyCoverage(),children);
						CptyLinkCollection::iterator ccur = children.begin();

						bool state = false;

						if(!state)
						{
							for(i=0;i<children.size();++i)
							{
								if(!creditReservation.isCptyCoverageNULL())
								{
									if( ((*ccur).second) ==psCpty)
									{
										state=true;
										break;
									}
								}
								++ccur;
							}

						}
						if(!state)
						{
							KNDB_T_ROLLBACK
								string errMsg(CreditLimit_Factory::instance()->className());
							errMsg+=" Reservation : Counterparty doesn't match with this Limit Definition";
							KGL_Response::sendFailure(KNC_FailureCategory::LOGICAL, errMsg.c_str(), handle);
							return;
						}
					}
				}

			}
			// end Cpty

			//////////////////////////////////////////////////////////////
			// folder
			if (!psCreditLimitMaster->FolderId_CoverageNULL())
			{
				if(!creditReservation.isFolderCoverageNULL())
				{
					KGR_Id knetId;
					if	(!KNCBTK_Identifier<FolderAlias_var
						 ,FolderAlias_Factory>
						 ::KNET_IdentifierToId(&creditReservation.getFolderCoverage()
											   ,handle->getSource()
											   ,knetId)
						)
					{
						;
					}
					Folder_var psFolder = KNCBTK_CoreBasic<Folder_var
						,Folder_Factory>::queryId(knetId);
					if (PS_is_nil(psFolder))
					{
						KNDB_T_ROLLBACK
							string errMsg(Folder_Factory::instance()->className());
						errMsg+=" not found";
						KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
						return;
					}
					if(psCreditLimitMaster->arcFolderCoverage() ==psFolder)
					{
					}
					else
					{
						unsigned long i;
						FolderLinkCollection children;
						FolderLink_Factory::instance()->queryChildren(psCreditLimitMaster->arcFolderCoverage(),children);
						FolderLinkCollection::iterator ccur = children.begin();

						bool state = false;
						if(!state)
						{
							for(i=0;i<children.size();++i)
							{
								if(!creditReservation.isFolderCoverageNULL())
								{
									if( ((*ccur).second) ==psFolder)
									{
										state=true;
										break;
									}
								}
								++ccur;
							}

						}
						if(!state)
						{
							KNDB_T_ROLLBACK
								string errMsg(CreditLimit_Factory::instance()->className());
							errMsg+=" Reservation : Folder doesn't match with this Limit Definition";
							KGL_Response::sendFailure(KNC_FailureCategory::LOGICAL, errMsg.c_str(), handle);
							return;
						}
					}
				}

			}
			// end Folder

			//////////////////////////////////////////////////////////////
			// Country
			if (!psCreditLimitMaster->CountryId_CoverageNULL())
			{
				if(!creditReservation.isCountryCoverageNULL())
				{
					KGR_Id knetId;
					if	(!KNCBTK_Identifier<CountryAlias_var
						 ,CountryAlias_Factory>
						 ::KNET_IdentifierToId(&creditReservation.getCountryCoverage()
											   ,handle->getSource()
											   ,knetId)
						)
					{
						;
					}
					Country_var psCountry = KNCBTK_CoreBasic<Country_var
						,Country_Factory>::queryId(knetId);
					if (PS_is_nil(psCountry))
					{
						KNDB_T_ROLLBACK
							string errMsg(Country_Factory::instance()->className());
						errMsg+=" not found";
						KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
						return;
					}
					if(psCreditLimitMaster->arcCountryCoverage() ==psCountry)
					{
					}
					else
					{
						unsigned long i;
						CountryLinkCollection children;
						CountryLink_Factory::instance()->queryChildren(psCreditLimitMaster->arcCountryCoverage(),children);
						CountryLinkCollection::iterator ccur = children.begin();

						bool state = false;

						if(!state)
						{
							for(i=0;i<children.size();++i)
							{
								if(!creditReservation.isCountryCoverageNULL())
								{
									if( ((*ccur).second) ==psCountry)
									{
										state=true;
										break;
									}
								}
								++ccur;
							}

						}
						if(!state)
						{
							KNDB_T_ROLLBACK
								string errMsg(CreditLimit_Factory::instance()->className());
							errMsg+=" Reservation : Country doesn't match with this Limit Definition";
							KGL_Response::sendFailure(KNC_FailureCategory::LOGICAL, errMsg.c_str(), handle);
							return;
						}
					}
				}

			}
			// end Country

			//////////////////////////////////////////////////////////////
			// Industry
			if (!psCreditLimitMaster->IndustryId_CoverageNULL())
			{
				if(!creditReservation.isIndustryCoverageNULL())
				{
					KGR_Id knetId;
					if	(!KNCBTK_Identifier<IndustryAlias_var
						 ,IndustryAlias_Factory>
						 ::KNET_IdentifierToId(&creditReservation.getIndustryCoverage()
											   ,handle->getSource()
											   ,knetId)
						)
					{
						;
					}
					Industry_var psIndustry = KNCBTK_CoreBasic<Industry_var
						,Industry_Factory>::queryId(knetId);
					if (PS_is_nil(psIndustry))
					{
						KNDB_T_ROLLBACK
							string errMsg(Industry_Factory::instance()->className());
						errMsg+=" not found";
						KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
						return;
					}
					if(psCreditLimitMaster->arcIndustryCoverage() ==psIndustry)
					{
					}
					else
					{
						unsigned long i;

						IndustryLinkCollection children;
						IndustryLink_Factory::instance()->queryChildren(psCreditLimitMaster->arcIndustryCoverage(),children);
						IndustryLinkCollection::iterator ccur = children.begin();

						bool state = false;

						if(!state)
						{
							for(i=0;i<children.size();++i)
							{
								if(!creditReservation.isIndustryCoverageNULL())
								{
									if( ((*ccur).second) ==psIndustry)
									{
										state=true;
										break;
									}
								}
								++ccur;
							}

						}
						if(!state)
						{
							KNDB_T_ROLLBACK
								string errMsg(CreditLimit_Factory::instance()->className());
							errMsg+=" Reservation : Industry doesn't match with this Limit Definition ";
							KGL_Response::sendFailure(KNC_FailureCategory::LOGICAL, errMsg.c_str(), handle);
							return;
						}
					}
				}

			}
			// end Industry

			//////////////////////////////////////////////////////////////
			// Currency
			if (!psCreditLimitMaster->CurrencyId_CoverageNULL())
			{
				if(!creditReservation.isCurrencyCoverageNULL())
				{
					KGR_Id knetId;
					if	(!KNCBTK_Identifier<CurrencyAlias_var
						 ,CurrencyAlias_Factory>
						 ::KNET_IdentifierToId(&creditReservation.getCurrencyCoverage()
											   ,handle->getSource()
											   ,knetId)
						)
					{
						;
					}
					Currency_var psCurrency = KNCBTK_CoreBasic<Currency_var
						,Currency_Factory>::queryId(knetId);
					if (PS_is_nil(psCurrency))
					{
						KNDB_T_ROLLBACK
							string errMsg(Currency_Factory::instance()->className());
						errMsg+=" not found";
						KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
						return;
					}
					if(psCreditLimitMaster->arcCurrencyCoverage() ==psCurrency)
					{
					}
					else
					{
						unsigned long i;
						CurrencyLinkCollection children;
						CurrencyLink_Factory::instance()->queryChildren(psCreditLimitMaster->arcCurrencyCoverage(),children);
						CurrencyLinkCollection::iterator ccur = children.begin();

						bool state = false;
						if(!state)
						{
							for(i=0;i<children.size();++i)
							{
								if(!creditReservation.isCurrencyCoverageNULL())
								{
									if( ((*ccur).second) ==psCurrency)
									{
										state=true;
										break;
									}
								}
								++ccur;
							}

						}
						if(!state)
						{
							KNDB_T_ROLLBACK
								string errMsg(CreditLimit_Factory::instance()->className());
							errMsg+=" Reservation : Currency doesn't match with this Limit Definition ";
							KGL_Response::sendFailure(KNC_FailureCategory::LOGICAL, errMsg.c_str(), handle);
							return;
						}
					}
				}

			}
			// end Currency

			//////////////////////////////////////////////////////////////
			// KNUser
			if (!psCreditLimitMaster->KNUserId_CoverageNULL())
			{
				if(!creditReservation.isUserCoverageNULL())
				{
					KGR_Id knetId;
					if	(!KNCBTK_Identifier<KNUserAlias_var
						 ,KNUserAlias_Factory>
						 ::KNET_IdentifierToId(&creditReservation.getUserCoverage()
											   ,handle->getSource()
											   ,knetId)
						)
					{
						;
					}
					KNUser_var psUser = KNCBTK_CoreBasic<KNUser_var
						,KNUser_Factory>::queryId(knetId);
					if (PS_is_nil(psUser))
					{
						KNDB_T_ROLLBACK
							string errMsg(KNUser_Factory::instance()->className());
						errMsg+=" not found";
						KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
						return;
					}
					TODO("enum");
					if (psUser->Purpose().buff()[0]=='A')
					{
						throw_LOGICAL(" User Coverage should have User Identification as Purpose");
					}

					if(psCreditLimitMaster->arcKNUserCoverage() ==psUser)
					{
					}
					else
					{
						unsigned long i;
						KNUserLinkCollection children;
						KNUserLink_Factory::instance()->queryChildren(psCreditLimitMaster->arcKNUserCoverage(),children);
						KNUserLinkCollection::iterator ccur = children.begin();

						bool state = false;

						if(!state)
						{
							for(i=0;i<children.size();++i)
							{
								if(!creditReservation.isUserCoverageNULL())
								{
									if( ((*ccur).second) ==psUser)
									{
										state=true;
										break;
									}
								}
								++ccur;
							}

						}
						if(!state)
						{
							KNDB_T_ROLLBACK
								string errMsg(CreditLimit_Factory::instance()->className());
							errMsg+=" Reservation : User doesn't match with this Limit Definition ";
							KGL_Response::sendFailure(KNC_FailureCategory::LOGICAL, errMsg.c_str(), handle);
							return;
						}
					}
				}

			}
			// end User

			//////////////////////////////////////////////////////////////
			// instrument
			if(!creditReservation.isInstrumentCoverageNULL())
			{
				KGR_Id knetId;
				if	(!KNCBTK_Identifier<InstrumentAlias_var
					 ,InstrumentAlias_Factory>
					 ::KNET_IdentifierToId(&creditReservation.getInstrumentCoverage()
										   ,handle->getSource()
										   ,knetId)
					)
				{
					;
				}

				Instrument_var psInstrument = KNCBTK_CoreBasic<Instrument_var
					,Instrument_Factory>::queryId(knetId);
				if (PS_is_nil(psInstrument))
				{
					KNDB_T_ROLLBACK
						string errMsg(Instrument_Factory::instance()->className());
					errMsg+=" not found";
					KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
					return;
				}

			}


			//////////////////////////////////////////////////////////////
			// Rating Agency
			if (!psCreditLimitMaster->RatingAgencyIdNULL())
			{
				if(!creditReservation.isRatingAgencyCoverageNULL())
				{
					KGR_Id knetId;
					if	(!KNCBTK_Identifier<RatingAgencyAlias_var
						 ,RatingAgencyAlias_Factory>
						 ::KNET_IdentifierToId(&creditReservation.getRatingAgencyCoverage()
											   ,handle->getSource()
											   ,knetId)
						)
					{
						;
					}
					RatingAgency_var psRatingAgency = KNCBTK_CoreBasic<RatingAgency_var
						,RatingAgency_Factory>::queryId(knetId);
					if (PS_is_nil(psRatingAgency))
					{
						KNDB_T_ROLLBACK
							string errMsg(RatingAgency_Factory::instance()->className());
						errMsg+=" not found";
						KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
						return;
					}
					if(psCreditLimitMaster->arcRatingAgency() ==psRatingAgency)
					{
					}
					else
					{
						KNDB_T_ROLLBACK
							string errMsg(CreditLimit_Factory::instance()->className());
						errMsg+=" Reservation : RatingAgency doesn't match with this Limit Definition";
						KGL_Response::sendFailure(KNC_FailureCategory::LOGICAL, errMsg.c_str(), handle);
						return;
					}
				}

			}
			// end RatingAgency

			//////////////////////////////////////////////////////////////
			// rating
			if (!psCreditLimitMaster->RatingId_CoverageNULL())
			{
				if(!creditReservation.isRatingCoverageNULL())
				{
					KGR_Id knetId;
					if	(!KNCBTK_Identifier<RatingAlias_var
						 ,RatingAlias_Factory>
						 ::KNET_IdentifierToId(&creditReservation.getRatingCoverage()
											   ,handle->getSource()
											   ,knetId)
						)
					{
						;
					}
					Rating_var psRating = KNCBTK_CoreBasic<Rating_var
						,Rating_Factory>::queryId(knetId);
					if (PS_is_nil(psRating))
					{
						KNDB_T_ROLLBACK
							string errMsg(Rating_Factory::instance()->className());
						errMsg+=" not found";
						KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
						return;
					}
					if(psCreditLimitMaster->arcRatingCoverage() ==psRating)
					{
					}
					else
					{
						unsigned long i;
						RatingLinkCollection children;
						RatingLink_Factory::instance()->queryChildren(psCreditLimitMaster->arcRatingCoverage(),children);
						RatingLinkCollection::iterator ccur = children.begin();

						bool state = false;

						if(!state)
						{
							for(i=0;i<children.size();++i)
							{
								if(!creditReservation.isRatingCoverageNULL())
								{
									if( ((*ccur).second) ==psRating)
									{
										state=true;
										break;
									}
								}
								++ccur;
							}

						}
						if(!state)
						{
							KNDB_T_ROLLBACK
								string errMsg(CreditLimit_Factory::instance()->className());
							errMsg+=" Reservation : Rating doesn't match with this Limit Definition ";
							KGL_Response::sendFailure(KNC_FailureCategory::LOGICAL, errMsg.c_str(), handle);
							return;
						}
					}
				}

			}

			// TOTOF SEE LIMIT COVERAGE TEST


			//


			CreditReservation_var createdCreditReservation
				= createCreditReservationFromKNET(handle, psCreditLimit, creditReservation);

			KNDB_T_COMMIT

				kncbtkAuditMsg_CreditReservation_.logInsert(handle->getUser()
															,createdCreditReservation
															,createdCreditReservation->Id(),1);

			KNC_Result res = KNET_DataResponse::sendInsertSuccess( KGR_Id( createdCreditReservation->Id()->getOidVal() ), handle );

			if(!res)
			{
				throw_LOGICAL( res.text() );
			};
			return;
		}
	catch (const PS_ServerError& e)
    {
		KNDB_T_ROLLBACK
			KNC_Result kncResultHE = KNDB_HANDLE_EXCEPTION(e);
		if (!kncResultHE)
        {
			ERROR_LOG << e.description << std::endl ;
			KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
			return;
        }
    }
	KNDB_LOOP_END
		}
/*
* onUpdateReservation (KNET_Id...)		!! CreditLimit specific !!
* ???UPDATE???
*/
void
KNCB_CreditLimit::onUpdateReservation (KGR_Id const& creditLimitMasterId,
                                       KGR_Id const* tbId,
                                       KGR_Id const& creditReservationId,
                                       KNET_CreditReservationChange const& creditReservation,
                                       KNET_RequestHandle handle)
{
	static const char* fctName = "KNCB_CreditLimit::onUpdateReservation";
	KH_DBG::dbg("KNCB_CreditLimit::onUpdateReservation::method_start");
	CreditLimit_var psCreditLimit;
	CreditLimitMaster_var psCreditLimitMaster;
	TimeBand_var psTB;
	TimeBandCoverageElt_var TBElement;
	//
	try
    {

		//string st=	KNETToStringId(*tbId, true ) ;
		//if(!strcmp("0x000000000000000000000000",st.c_str()))
		if (!tbId || !strlen(tbId->getValue()))
			//time band 0D+-
			psTB = TimeBand_Factory::instance()->queryShortName(string(INFINIT_TB_SHORTNAME).c_str());
		else
			psTB = KNCBTK_CoreBasic<TimeBand_var ,TimeBand_Factory>
				::queryId(*tbId);

		PS_Oid_var userOid(new PS_Oid);
		userOid->setOidVal((const unsigned char*)(handle->getUser()).getValue());
		psCreditLimitMaster = KNCBTK_CoreBasic<CreditLimitMaster_var
			,CreditLimitMaster_Factory>
			::queryId(creditLimitMasterId);


		if (PS_is_nil(psCreditLimitMaster))
        {
			string errMsg(CreditLimitMaster_Factory::instance()->className());
			errMsg+="Not Found ";
			//KNET_CreditLimitResponse::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
			KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
			return;
        }



		if (PS_is_nil(psTB))
        {
			string errMsg(TimeBand_Factory::instance()->className());
			errMsg+="Not Found ";
			//KNET_CreditLimitResponse::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
			KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
			return;
        }


		if(!CreditLimitMaster_Factory::instance()->hasAccess(false,true,psCreditLimitMaster,userOid))
        {
			throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }
		if(!PS_is_nil(psCreditLimitMaster->arcCptyCoverage()) &&
		   !Cpty_Factory::instance()->hasAccess(2,false,true,psCreditLimitMaster->arcCptyCoverage(),userOid))
        {
			throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }
		if(!PS_is_nil(psCreditLimitMaster->arcFolderCoverage()) &&
		   !Folder_Factory::instance()->hasAccess(2,false,true,psCreditLimitMaster->arcFolderCoverage(),userOid))
        {
			throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }
    }
	catch (const PS_UserError& e)
    {
		ERROR_LOG << e.description() << std::endl ;
		failure(e, handle);
		return;
    }
	catch (const PS_ServerError& e)
    {
		//				ERROR_LOG << e.description() << std::endl ;
		failure(e, handle);
		return;
    }
	try
    {
		if (!hasTableAccess(UPD
							,CreditReservation_Factory::instance()->className()
							,handle->getUser()))
			return;
		//
    }
	catch (const PS_UserError& e)
    {
		
		WARNING_LOG << e.description()<< std::endl;
		KGL_Response::sendFailure(KNC_FailureCategory::SECURITY, e.description(), handle);
		return;
    }
	catch (const PS_ServerError& e)
    {
		ERROR_LOG << fctName <<": caught exception PS_ServerError, nm=" << (const char*)(e.name);
		ERROR_LOG << ", descr=" << (const char*)(e.description) << ", excpNm" << (const char*)(e.exceptionName()) << endl;
		KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
		return;
    }
	KNDB_LOOP_BEGIN
		try
		{
			//
			KNDB_T_WRITE
				//
				PS_Oid_var userOid(new PS_Oid);
			userOid->setOidVal((const unsigned char*)(handle->getUser()).getValue());
			PS_Oid_var officeOid;
			bool status=KNETUserIdToPSOfficeId(handle->getUser(), officeOid);


			if(status &&!CreditLimitMaster_Factory::instance()->hasAccess(false,true,psCreditLimitMaster,userOid))
			{
				throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
			}
			if(status &&!PS_is_nil(psCreditLimitMaster->arcCptyCoverage()) &&
			   !Cpty_Factory::instance()->hasAccess(2,false,true,psCreditLimitMaster->arcCptyCoverage(),userOid))
			{
				throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
			}
			if(status &&!PS_is_nil(psCreditLimitMaster->arcFolderCoverage()) &&
			   !Folder_Factory::instance()->hasAccess(2,false,true,psCreditLimitMaster->arcFolderCoverage(),userOid))
			{
				throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
			}

			//

			KGLDB_WhereClause whereClause;
			whereClause.addCondition( "CreditLimitMasterId", "=", KGR_Id(psCreditLimitMaster->Id()->getOidVal()) );
			whereClause.addCondition( "TimeBandId", "=", KGR_Id(psTB->Id()->getOidVal()) );

			CreditLimit_Cltn_var CLColl = CreditLimit_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());

			if(!PS_is_nil(CLColl) && 0 != CLColl->length())
			{
				psCreditLimit = CLColl[ 0ul ];
			}
			else
			{
				throw_NOTFOUND(CreditLimit_Factory::instance()->className());
			}

			if( psCreditLimit->AllocatedAmount() <creditReservation.getAllocatedAmount())
			{
				KNDB_T_ROLLBACK
					string errMsg(CreditLimit_Factory::instance()->className());
				errMsg+=" reservation amount larger than the limit";
				KGL_Response::sendFailure(KNC_FailureCategory::LOGICAL, errMsg.c_str(), handle);
				return;
			}

			CreditReservation_var toUpdateCreditReservation =
				KNCBTK_CoreBasic<CreditReservation_var,CreditReservation_Factory>
				::queryId(creditReservationId);

			if (PS_is_nil(toUpdateCreditReservation))
			{
				KNDB_T_ROLLBACK
					string errMsg(CreditReservation_Factory::instance()->className());
				errMsg+=" not found";
				KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
				return;
			}
			//

			kncbtkAuditMsg_CreditReservation_.logPreUpdate(toUpdateCreditReservation,1);
			KNETToPSCreditReservation(handle
									  ,psCreditLimit
									  ,creditReservation
									  ,toUpdateCreditReservation);

			KNDB_T_COMMIT

				kncbtkAuditMsg_CreditReservation_.logPostUpdate(handle->getUser()
																,toUpdateCreditReservation
																,toUpdateCreditReservation->Id(),1);

			KNC_Result res = KNET_DataResponse::sendUpdateSuccess( handle );

			if(!res)
			{
				throw_LOGICAL(res.text());
			};
			return;

		}
	catch (const PS_ServerError& e)
    {
		KNDB_T_ROLLBACK
			KNC_Result kncResultHE
			= KNDB_HANDLE_EXCEPTION(e);
		if (!kncResultHE)
        {
			ERROR_LOG << e.description << std::endl ;
			KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
			return;
        }
    }
	KNDB_LOOP_END
	KH_DBG::dbg("KNCB_CreditLimit::onUpdateReservation::method_end");
		}
/*
* onRemoveReservation (KNET_Id...)		!! CreditLimit specific !!
* ???REMOVE???
* ???DELETE???
*/
void
KNCB_CreditLimit::onRemoveReservation (KGR_Id const& creditReservationId,
                                       KNET_RequestHandle handle)
{
  static const char* fctName = "KNCB_CreditLimit::onRemoveReservation";
  KH_DBG::dbg("KNCB_CreditLimit::onRemoveReservation::method_start");
  //
  try
    {
      if (!hasTableAccess(DEL
                          ,CreditReservation_Factory::instance()->className()
                          ,handle->getUser()))
        return;
      //
    }
  catch (const PS_UserError& e)
    {
      
      WARNING_LOG << e.description()<< std::endl;
      KGL_Response::sendFailure(KNC_FailureCategory::SECURITY, e.description(), handle);
      return;
    }
  catch (const PS_ServerError& e)
    {
		ERROR_LOG << fctName <<": caught exception PS_ServerError, nm=" << (const char*)(e.name);
		ERROR_LOG << ", descr=" << (const char*)(e.description) << ", excpNm" << (const char*)(e.exceptionName()) << endl;
      KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
      return;
    }
  KNDB_LOOP_BEGIN
  try
    {
      //
      KNDB_T_WRITE
      CreditReservation_var toDeleteCreditReservation = KNCBTK_CoreBasic<CreditReservation_var
          ,CreditReservation_Factory>
          ::queryId(creditReservationId);
      if (PS_is_nil(toDeleteCreditReservation))
        {
          KNDB_T_ROLLBACK
          string errMsg(CreditReservation_Factory::instance()->className());
          errMsg+=" not found";
          KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
          return;
        }
      //
      PS_Oid_var officeOid;
      PS_Oid_var userOid(new PS_Oid);
      userOid->setOidVal((const unsigned char*)(handle->getUser()).getValue());
      bool status=KNETUserIdToPSOfficeId(handle->getUser(), officeOid);


      //le test d'access se fait sur la master
      CreditLimitMaster_var psCreditLimitMaster = CreditLimitMaster_Factory::instance()->queryKey(*toDeleteCreditReservation->arcCreditLimit()->CreditLimitMasterId(), PS_Defs::k_cacheThenDatabase) ;

      if (PS_is_nil(psCreditLimitMaster))
        {
          KNDB_T_ROLLBACK
          string errMsg(CreditLimitMaster_Factory::instance()->className());
          errMsg+=" not found";
          KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
          return;
        }

      if(status &&!CreditLimitMaster_Factory::instance()->hasAccess(false,true,psCreditLimitMaster,userOid))
        {
          throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }
      if(status &&!PS_is_nil(psCreditLimitMaster->arcCptyCoverage()) &&
          !Cpty_Factory::instance()->hasAccess(2,false,true,psCreditLimitMaster->arcCptyCoverage(),userOid))
        {
          throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }
      if(status &&!PS_is_nil(psCreditLimitMaster->arcFolderCoverage()) &&
          !Folder_Factory::instance()->hasAccess(2,false,true,psCreditLimitMaster->arcFolderCoverage(),userOid))
        {
          throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }

		kncbtkAuditMsg_CreditReservation_.logPrepareDelete(handle->getUser()
          ,toDeleteCreditReservation
          ,toDeleteCreditReservation->Id(),1);
      CreditReservation_Factory::instance()->remove
      (toDeleteCreditReservation);
      KNDB_T_COMMIT
      kncbtkAuditMsg_CreditReservation_.logCommitDelete(1);

      KNC_Result res = KNET_DataResponse::sendRemoveSuccess( handle );

      if(!res)
        {
          throw_LOGICAL(res.text());
        };
      return;
    }
  catch (const PS_ServerError& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
          KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
          return;
        }
    }
  KNDB_LOOP_END
  KH_DBG::dbg("KNCB_CreditLimit::onRemoveReservation::method_end");
}
/*
* onQueryReservation (KNET_Id...)		!! CreditLimit specific !!
*/
void
KNCB_CreditLimit::onQueryReservation (KGR_Id const& creditLimitMasterId,
                                      KGR_Id const* tbId,
                                      KNET_RequestHandle handle)
{
	TimeBand_var psTB;


	CreditLimitMaster_var psCreditLimitMaster;
	//
	try
    {
		PS_Oid_var userOid(new PS_Oid);
		userOid->setOidVal((const unsigned char*)(handle->getUser()).getValue());

		// string st=	KNETToStringId(*tbId, true ) ;

//		if(!strcmp("0x000000000000000000000000",st.c_str()))
		if (!tbId || !strlen(tbId->getValue()))
			//time band 0D+-
			psTB = TimeBand_Factory::instance()->queryShortName(string(INFINIT_TB_SHORTNAME).c_str());
		else
			psTB = KNCBTK_CoreBasic<TimeBand_var
				,TimeBand_Factory>::queryId(*tbId);

		psCreditLimitMaster = KNCBTK_CoreBasic<CreditLimitMaster_var
			,CreditLimitMaster_Factory>
			::queryId(creditLimitMasterId);

		if (PS_is_nil(psCreditLimitMaster))
        {
			string errMsg(CreditLimitMaster_Factory::instance()->className());
			errMsg+="Not Found ";
			KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
			return;
        }

		if(!CreditLimitMaster_Factory::instance()->hasAccess(true,false,psCreditLimitMaster,userOid))
        {
			throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }
		if(!PS_is_nil(psCreditLimitMaster->arcCptyCoverage()) &&
		   !Cpty_Factory::instance()->hasAccess(2,true,false,psCreditLimitMaster->arcCptyCoverage(),userOid))
        {
			throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }
		if(!PS_is_nil(psCreditLimitMaster->arcFolderCoverage()) &&
		   !Folder_Factory::instance()->hasAccess(2,true,false,psCreditLimitMaster->arcFolderCoverage(),userOid))
        {
			throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }
    }
	catch (const PS_UserError& e)
    {
		ERROR_LOG << e.description() << std::endl ;
		failure(e, handle);
		return;
    }
	catch (const PS_ServerError& e)
    {
		failure(e, handle);
		return;
    }
	KNDB_LOOP_BEGIN
		try
		{
			KGR_Collection<KNET_CreditReservationAccess> creditReservationCollection;
			KNDB_T_READ

				PS_Oid_var officeOid;
			PS_Oid_var userOid(new PS_Oid);
			userOid->setOidVal((const unsigned char*)(handle->getUser()).getValue());
			bool status=KNETUserIdToPSOfficeId(handle->getUser(), officeOid);


			if(status &&!CreditLimitMaster_Factory::instance()->hasAccess(true,false,psCreditLimitMaster,userOid))
			{
				throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
			}

			if(status &&!PS_is_nil(psCreditLimitMaster->arcCptyCoverage()) &&
			   !Cpty_Factory::instance()->hasAccess(2,true,false,psCreditLimitMaster->arcCptyCoverage(),userOid))
			{
				throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
			}
			if(status &&!PS_is_nil(psCreditLimitMaster->arcFolderCoverage()) &&
			   !Folder_Factory::instance()->hasAccess(2,true,false,psCreditLimitMaster->arcFolderCoverage(),userOid))
			{
				throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
			}

			KGLDB_WhereClause whereClause;
			whereClause.addCondition( "CreditLimitMasterId", "=", KGR_Id(psCreditLimitMaster->Id()->getOidVal()) );
			whereClause.addCondition( "TimeBandId", "=", KGR_Id(psTB->Id()->getOidVal()) );

			TimeBandCoverageElt_Cltn_var collTimeBandElts =	TimeBandCoverageElt_Factory::instance()->querySQLWhere( whereClause.getConditions().c_str() );

			if(collTimeBandElts->length() == 0)
			{
				//infinite limit no TB elements

				whereClause.erase();
				whereClause.addCondition( "CreditLimitMasterId", "=", KGR_Id(psCreditLimitMaster->Id()->getOidVal()) );
				whereClause.addCondition( "TimeBandId", "=", KGR_Id(psTB->Id()->getOidVal()) );
				CreditLimit_Cltn_var CLColl = CreditLimit_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());

				if(!PS_is_nil(CLColl) && 0!=CLColl->length())
				{
					CreditLimit_var psCreditLimit = CLColl[0ul];

					whereClause.erase();
					whereClause.addCondition( "CreditLimitId", "=", KGR_Id(psCreditLimit->Id()->getOidVal()) );
					// to exclude allocation transfert
					whereClause.addExpression("AND CreditLimitId_Transfer is NULL");
					whereClause.addExpression("AND CreditReservationId_Transfer is NULL");

					CreditReservation_Cltn_var creditReservationColl =
						CreditReservation_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());

					if(!PS_is_nil(creditReservationColl))
                                        {
                                                unsigned long collSize = creditReservationColl->length();
                                                for (unsigned long i=0; i<collSize; ++i )
                                                {
                                                        KNET_CreditReservationAccess knetCreditReservation;
                                                        CreditReservation_var CR=creditReservationColl[(unsigned long) i];

                                                        PSToKNETCreditReservation(CR, knetCreditReservation);

                                                        creditReservationCollection.push_back(knetCreditReservation);
                                                }
                                        }
				}
			}
			unsigned long k;
			for(k=0;k<collTimeBandElts->length();k++)
			{
				TimeBandCoverageElt_var TBElement;

				TBElement= collTimeBandElts[(unsigned long)k] ;

				//pour chacun des element de la master on va chercher la creditlimit associee
				whereClause.erase();
				whereClause.addCondition( "CreditLimitMasterId", "=", KGR_Id(TBElement->CreditLimitMasterId()->getOidVal()) );
				whereClause.addCondition( "TimeBandId", "=", KGR_Id(TBElement->TimeBandId()->getOidVal()) );
				CreditLimit_Cltn_var CLColl = CreditLimit_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());

				if(!PS_is_nil(CLColl) && 0!=CLColl->length())
				{
					CreditLimit_var psCreditLimit = CLColl[0ul];

					whereClause.erase();
					whereClause.addCondition( "CreditLimitId", "=", KGR_Id(psCreditLimit->Id()->getOidVal()) );
					// to exclude allocation transfert
					whereClause.addExpression("AND CreditLimitId_Transfer is NULL");
					whereClause.addExpression("AND CreditReservationId_Transfer is NULL");

					CreditReservation_Cltn_var creditReservationColl = CreditReservation_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());

					//
					if(!PS_is_nil(creditReservationColl))
					{
						unsigned long collSize = creditReservationColl->length();
						for (unsigned long i=0; i<collSize; ++i )
						{
							KNET_CreditReservationAccess knetCreditReservation;
							CreditReservation_var CR=creditReservationColl[ i ];

							PSToKNETCreditReservation(CR, knetCreditReservation);

							creditReservationCollection.push_back(knetCreditReservation);
						}
					}
				}
			}

			KNDB_T_COMMIT
				KNC_Result res=KNCB_CreditLimit::RELATED_VALIDATION_RESPONSE_CLASS::sendQueryReservationSuccess(creditReservationCollection
																												,handle);
			if(!res)
			{
				throw_LOGICAL(res.text());
			};
			return;
		}
	catch (const PS_ServerError& e)
    {
		KNDB_T_ROLLBACK
			KNC_Result kncResultHE
			= KNDB_HANDLE_EXCEPTION(e);
		if (!kncResultHE)
        {
			ERROR_LOG << e.description << std::endl ;
			KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
			return;
        }
    }
	KNDB_LOOP_END
		}
/*
* onQueryReservationDeal (KNET_Id...)		!! CreditLimit specific !!
*/
void
KNCB_CreditLimit::onQueryReservationDeal (KGR_Id const& creditReservationId,
    KNET_RequestHandle handle)
{
  //
  KNDB_LOOP_BEGIN
  try
    {

      KGR_Collection<KNET_CreditDeal> creditDealCollection;
      KNDB_T_READ
      CreditReservation_var psCreditReservation = KNCBTK_CoreBasic<CreditReservation_var
          ,CreditReservation_Factory>
          ::queryId(creditReservationId);
      if (PS_is_nil(psCreditReservation))
        {
          KNDB_T_ROLLBACK
          string errMsg(CreditReservation_Factory::instance()->className());
          errMsg+=" not found";
          KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
          return;
        }
      PS_Oid_var officeOid;
      PS_Oid_var userOid(new PS_Oid);
      userOid->setOidVal((const unsigned char*)(handle->getUser()).getValue());
      bool status=KNETUserIdToPSOfficeId(handle->getUser(), officeOid);


      CreditLimitMaster_var CLM= CreditLimitMaster_Factory::instance()->queryKey(*psCreditReservation->arcCreditLimit()->CreditLimitMasterId(), PS_Defs::k_cacheThenDatabase) ;

      if (PS_is_nil(CLM))
        {
          KNDB_T_ROLLBACK
          string errMsg(CreditLimitMaster_Factory::instance()->className());
          errMsg+=" not found";
          KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
          return;
        }

      if(status &&!CreditLimitMaster_Factory::instance()->hasAccess(true,false,CLM ,userOid))
        //if(status &&!KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->hasAccess(true,false,psCreditReservation->arcCreditLimit(),userOid))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }
      if(status &&!PS_is_nil(CLM->arcCptyCoverage()) &&
          !Cpty_Factory::instance()->hasAccess(2,true,false,CLM->arcCptyCoverage(),userOid))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }
      if(status &&!PS_is_nil(CLM->arcFolderCoverage()) &&
          !Folder_Factory::instance()->hasAccess(2,true,false,CLM->arcFolderCoverage(),userOid))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }


      //
      string searchCondition("CreditReservationId = 0x");
      string idStr = KNC_ConvId::idToStr((const char*)psCreditReservation->Id()->getOidVal());
      searchCondition+=idStr;

      CreditReservationDeal_Cltn_var cltn
      = CreditReservationDeal_Factory::instance()->querySQLWhere(searchCondition.c_str());
      unsigned long totalCount=cltn->length();
      //
      if (totalCount==0)
        {
          KNDB_T_ROLLBACK
          string errMsg(CreditReservationDeal_Factory::instance()->className());
          errMsg+=" not found";
          KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
          return;
        }
      //
      DealLog_var psDealLog;
      long creditLeg;
      CreditLog_var psCreditLog;

      unsigned long i= (unsigned long) 0.0;
      for (;i<totalCount;++i)
        {
          
          psDealLog = DealLog_var::narrow(cltn[(unsigned long) i]->arcDealLog());
          
          creditLeg = cltn[(unsigned long) i]->CreditLeg();
          psCreditLog = CreditLog_Factory::instance()->queryKey(*psDealLog->Id() // const PS_Oid& DealLogId
                        ,creditLeg // long CreditLeg
                        ,PS_Defs::k_cacheThenDatabase);
          if (PS_is_nil(psCreditLog))
            {
              KNDB_T_ROLLBACK
              string errMsg(CreditLog_Factory::instance()->className());
              errMsg+=" not found";
              KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
              return;
            }
          //
          KNET_CreditDeal knetCreditDeal;
          PSToKNETCreditDeal(psDealLog
                             ,psCreditLog
                             ,knetCreditDeal);

          creditDealCollection.push_back(knetCreditDeal);

        }
      KNDB_T_COMMIT
      KNC_Result res=KNCB_CreditLimit::RELATED_VALIDATION_RESPONSE_CLASS::sendQueryReservationDealSuccess(creditDealCollection
                     ,handle);
      if(!res)
        {
          throw_LOGICAL(res.text());
        };
      return;
    }
  catch (const PS_ServerError& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
          KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
          return;
        }
    }
  KNDB_LOOP_END
}


double
KNCB_CreditLimit_getRate(CreditLimitMaster_var const& creditLimitSource,
                         CreditLimitMaster_var const& creditLimitDestination)
{
  static const char*fctName = "KNCB_CreditLimit_getRate";
  double rate = 1.0;
  TODO("003");
  if(*creditLimitSource->CurrencyId() ==
      *creditLimitDestination->CurrencyId())
    {
      //same currency
    }
  else
    {
      // fetch pair DestCur/SourceCur
      // to convert transfert amount in sourceCur
      try
        {
          KGLDB_WhereClause whereClause;
          string expr("CurrencyId_1 = ");
          expr.append(KNETToStringId(
                        KGR_Id(creditLimitDestination->CurrencyId()->getOidVal()),
                        true));
          expr.append(" AND CurrencyId_2 = " );
          expr.append(KNETToStringId(
                        KGR_Id(creditLimitSource->CurrencyId()->getOidVal()),
                        true));
          whereClause.addExpression(expr.c_str());
          Pair_Cltn_var pairCltn = Pair_Factory::instance()->querySQLWhere(
                                     whereClause.getConditions().c_str());

          if(!PS_is_nil(pairCltn) && pairCltn->length())
            {
              
              Pair_var pair = pairCltn[(unsigned long) 0];
              char psQuotation = *(pair->QuotationMode().buff());
              KNET_CurrencyPair::QuotationMode qMode;
              if(psQuotation == KNDBC_Choices::QUOTATION_MODE_INDIRECT)
                qMode = KNET_CurrencyPair::KNET_INDIRECT;
              if(psQuotation == KNDBC_Choices::QUOTATION_MODE_DIRECT)
                qMode = KNET_CurrencyPair::KNET_DIRECT;

              rate = KF_Pair::Spot_GetAmount2( 1.0, pair->SpotRate(),
                                               pair->Quotation(), qMode) ;
            }
        }
      catch (const PS_ServerError& e)
        {
		ERROR_LOG << fctName <<": caught exception PS_ServerError, nm=" << (const char*)(e.name);
		ERROR_LOG << ", descr=" << (const char*)(e.description) << ", excpNm" << (const char*)(e.exceptionName()) << endl;
        }

    }

  return rate;
}

double KNCB_CreditLimit::getReservedAmount(const CreditLimit_var &sourceId,  const KGR_Id &updateReservation)
{
	double result = 0;

	KGLDB_WhereClause whereClause;
	whereClause.addCondition( "CreditLimitId", "=", sourceId->Id() );
	if( updateReservation != KGR_Id::EMPTY_ID ) {
		whereClause.addCondition( "Id", "!=", updateReservation );
	}

	CreditReservation_Iter_var transfers =
			CreditReservation_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());
	while( transfers->hasNext() ) {
		CreditReservation_var transfer =
				transfers->next();
		result += transfer->AllocatedAmount();
	}

	return result;
}

/*
* onInsertReservationTransfer (KNET_Id...)		!! CreditLimit specific !!
*/
void
KNCB_CreditLimit::onInsertReservationTransfer (KGR_Id const& creditLimitMasterSourceId,	//master limit
    KGR_Id const& creditLimitMasterDestinationId,		//master limit
    KGR_Id const& creditTBSourceId,	//TB source
    KGR_Id const& creditTBDestinationId,		//TB destination
    KNET_CreditReservationTransferChange const& creditReservationTransfer,
    KNET_RequestHandle handle)
{
	static const char* fctName = "KNCB_CreditLimit::onInsertReservationTransfer";

	CreditLimit_var psCreditLimitSource;
	CreditLimit_var psCreditLimitDestination;

	char buffer[255];

	//
	try
    {
		if (!hasTableAccess(INS
							,CreditReservation_Factory::instance()->className()
							,handle->getUser()))
			return;
		//
    }
	catch (const PS_UserError& e)
    {
		
		WARNING_LOG << e.description()<< std::endl;
		KGL_Response::sendFailure(KNC_FailureCategory::SECURITY, e.description(), handle);
		return;
    }
	catch (const PS_ServerError& e)
    {
		ERROR_LOG << fctName <<": caught exception PS_ServerError, nm=" << (const char*)(e.name);
		ERROR_LOG << ", descr=" << (const char*)(e.description) << ", excpNm" << (const char*)(e.exceptionName()) << endl;
		KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
		return;
    }
	KNDB_LOOP_BEGIN
		try
		{
			//get the CL source Id from his masterId/timeId
			KGLDB_WhereClause whereClause;
			whereClause.addCondition( "CreditLimitMasterId", "=", creditLimitMasterSourceId );
			whereClause.addCondition( "TimeBandId", "=", creditTBSourceId );

			//TRACE_LOG << whereClause.getConditions().c_str() << endl;

			CreditLimit_Cltn_var CLColl = CreditLimit_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());

			if(!PS_is_nil(CLColl) && 0!=CLColl->length())
			{
				psCreditLimitSource = CLColl[ 0ul ];
			}
			else
			{
				throw_NOTFOUND(CreditLimit_Factory::instance()->className());
			}

			//get the CL destination Id from his masterId/timeId
			whereClause.erase();
			whereClause.addCondition( "CreditLimitMasterId", "=", creditLimitMasterDestinationId );
			whereClause.addCondition( "TimeBandId", "=", creditTBDestinationId );

			CLColl = CreditLimit_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());

			if(!PS_is_nil(CLColl) && 0!=CLColl->length())
			{
				psCreditLimitDestination = CLColl[ 0ul];
			}
			else
			{
				throw_NOTFOUND(CreditLimit_Factory::instance()->className());
			}

			//
			KNDB_T_WRITE
				//

				sprintf(buffer, "CreditLimitId=0x%s and CreditLimitId_Transfer=0x%s and CreditReservationId_Transfer is not NULL",
						KNC_ConvId::idToStr((const char*)psCreditLimitSource->Id()->getOidVal()).c_str(),
						KNC_ConvId::idToStr((const char*)psCreditLimitDestination->Id()->getOidVal()).c_str());

			CreditReservation_Cltn_var CRColl = CreditReservation_Factory::instance()->querySQLWhere(buffer);
			if (!PS_is_nil(CRColl) && CRColl->length()>0)
			{
				KNDB_T_ROLLBACK
					string errMsg(CreditReservation_Factory::instance()->className());
				errMsg+="Transfer already exists";
				KGL_Response::sendFailure(KNC_FailureCategory::LOGICAL, errMsg.c_str(), handle);
				return;
			}

			PS_Oid_var officeOid;
			PS_Oid_var userOid(new PS_Oid);
			userOid->setOidVal((const unsigned char*)(handle->getUser()).getValue());
			bool status=KNETUserIdToPSOfficeId(handle->getUser(), officeOid);

			//		if(IS_ACCESS_CHANGE())
			{
				if(status &&!CreditLimit_Factory::instance()->hasAccess(false,true,psCreditLimitSource,userOid))
				{
					throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
				}
				if(status &&!PS_is_nil(psCreditLimitSource->arcCreditLimitMaster()->arcCptyCoverage()) &&
				   !Cpty_Factory::instance()->hasAccess(2,false,true,psCreditLimitSource->arcCreditLimitMaster()->arcCptyCoverage(),userOid))
				{
					throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
				}
				if(status &&!PS_is_nil(psCreditLimitSource->arcCreditLimitMaster()->arcFolderCoverage()) &&
				   !Folder_Factory::instance()->hasAccess(2,false,true,psCreditLimitSource->arcCreditLimitMaster()->arcFolderCoverage(),userOid))
				{
					throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
				}
			}

			if(status &&!CreditLimit_Factory::instance()->hasAccess(false,true,psCreditLimitDestination,userOid))
			{
				throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
			}

			if(status &&!PS_is_nil(psCreditLimitDestination->arcCreditLimitMaster()->arcCptyCoverage()) &&
			   !Cpty_Factory::instance()->hasAccess(2,false,true,psCreditLimitDestination->arcCreditLimitMaster()->arcCptyCoverage(),userOid))
			{
				throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
			}
			if(status &&!PS_is_nil(psCreditLimitDestination->arcCreditLimitMaster()->arcFolderCoverage()) &&
			   !Folder_Factory::instance()->hasAccess(2,false,true,psCreditLimitDestination->arcCreditLimitMaster()->arcFolderCoverage(),userOid))
			{
				throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
			}

			CreditLimitMaster_var psCreditLimitMasterSource = CreditLimitMaster_Factory::instance()->queryKey(*psCreditLimitSource->CreditLimitMasterId(),PS_Defs::k_cacheThenDatabase) ;
			CreditLimitMaster_var psCreditLimitMasterDestination = CreditLimitMaster_Factory::instance()->queryKey(*psCreditLimitDestination->CreditLimitMasterId(),PS_Defs::k_cacheThenDatabase) ;

			if (PS_is_nil(psCreditLimitMasterSource) || PS_is_nil(psCreditLimitMasterDestination))
			{
				KNDB_T_ROLLBACK
					string errMsg(CreditLimit_Factory::instance()->className());
				errMsg+=" destination not found";
				KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
				return;
			}

			double rate = KNCB_CreditLimit_getRate(psCreditLimitMasterSource,
												   psCreditLimitMasterDestination);
			double psAllocatedAmountSource= rate*creditReservationTransfer.getAllocatedAmount();


			//we get the  of allocation according to the time band element source
			whereClause.erase();
			whereClause.addCondition( "CreditLimitMasterId", "=", creditLimitMasterSourceId );
			whereClause.addCondition( "TimeBandId", "=", creditTBSourceId );

			TimeBandCoverageElt_Cltn_var collTimeBandElts =	TimeBandCoverageElt_Factory::instance()->querySQLWhere( whereClause.getConditions().c_str() );

			double allocatedAmount = psCreditLimitMasterSource->AllocatedAmount();

			if(collTimeBandElts->length())
			{
				allocatedAmount =collTimeBandElts[(unsigned long)0]->AllocatedAmount();
			}

			if( allocatedAmount < (psAllocatedAmountSource + getReservedAmount(psCreditLimitSource, KGR_Id::EMPTY_ID)) )
			{
				KNDB_T_ROLLBACK
					string errMsg(CreditLimit_Factory::instance()->className());
				errMsg+=" reservation amount larger than the limit";
				KGL_Response::sendFailure(KNC_FailureCategory::LOGICAL, errMsg.c_str(), handle);
				return;
			}

			if(!(psCreditLimitMasterSource->arcCurrency()==psCreditLimitMasterDestination->arcCurrency()))
			{
				KNDB_T_ROLLBACK
					string errMsg(CreditLimit_Factory::instance()->className());
				errMsg+="  Can't insert a transfer on two limits with different currencies";
				KGL_Response::sendFailure(KNC_FailureCategory::LOGICAL, errMsg.c_str(), handle);
				return;
			}
			//
			CreditReservation_var createdCreditReservationTransferSource;
			CreditReservation_var createdCreditReservationTransferDestination;
			createCreditReservationTransferFromKNET(handle
													,psCreditLimitSource
													,psCreditLimitDestination
													,creditReservationTransfer
													,createdCreditReservationTransferSource
													,createdCreditReservationTransferDestination);
			KNDB_T_COMMIT
				kncbtkAuditMsg_CreditReservation_.logInsert(handle->getUser()
															,createdCreditReservationTransferSource,
															createdCreditReservationTransferSource->Id(),1);
			kncbtkAuditMsg_CreditReservation2_.logInsert(handle->getUser()
														 ,createdCreditReservationTransferDestination
														 ,createdCreditReservationTransferDestination->Id(),2);

			KNC_Result res = KNET_DataResponse::sendInsertSuccess( KGR_Id(createdCreditReservationTransferSource->Id()->getOidVal()),
																   handle );
			if(!res)
			{
				throw_LOGICAL(res.text());
			};

			/* Send asynchronous message (to the dashboard) */

			/* First, we have to get the inserted objects in a KNET_CreditReservationTransferAccess object */
			vector<KNET_CreditReservationTransferAccess> creditReservationTransferAccessCollection;
			CreditReservation_Cltn_var CRColl2 = CreditReservation_Factory::instance()->querySQLWhere(buffer);
			if (!PS_is_nil(CRColl2) && CRColl2->length() > 0)
			{
				unsigned long collSize = CRColl2->length();
				for ( unsigned long i=0; i<collSize; ++i )
				{
					KNET_CreditReservationTransferAccess knetCreditReservationTransferAccess;
					PSToKNETCreditReservationTransfer(CRColl2[i], knetCreditReservationTransferAccess);
					creditReservationTransferAccessCollection.push_back(knetCreditReservationTransferAccess);
				}
			}
			else
			{
				string errMsg(CreditLimit_Factory::instance()->className());
				errMsg+="No transfer inserted !";
				KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
				return;
			}

			/* Then, we send the message */
			KGL_CreditReservationTransferAdapterVectorImpl ResponseListObject;
			ResponseListObject.setRawData(creditReservationTransferAccessCollection);
			ResponseListObject.setObjectType(KGLE_AsyncFwkObjectType::CREDITRESERVATIONTRANSFER);
			KGLAF_AsyncFwk::instance().sendNotification(KGLE_AsyncMsgType::INSERTED,
														ResponseListObject,
														NULL);


			return;
		}
	catch (const PS_ServerError& e)
    {
		KNDB_T_ROLLBACK
			KNC_Result kncResultHE
			= KNDB_HANDLE_EXCEPTION(e);
		if (!kncResultHE)
        {
			ERROR_LOG << e.description << std::endl ;
			//A.G.:DO NOT SEND synchronous message for those treated in asynchronous mode
			//KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
			KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
			return;
        }
    }
	KNDB_LOOP_END
		}
/*
* onUpdateReservationTransfer (KNET_Id...)		!! CreditLimit specific !!
*/
void
KNCB_CreditLimit::onUpdateReservationTransfer (KGR_Id const& creditLimitMasterSourceId,
    KGR_Id const& creditLimitMasterDestinationId,
    KGR_Id const& creditTBSourceId,	//TB source
    KGR_Id const& creditTBDestinationId,		//TB destination
    KGR_Id const& creditReservationSourceId,
    KNET_CreditReservationTransferChange const& creditReservationTransfer,
    KNET_RequestHandle handle)
{
	static const char* fctName = "KNCB_CreditLimit::onUpdateReservationTransfer";
	CreditLimit_var psCreditLimitSource;
	CreditLimit_var psCreditLimitDestination;

	//
	try
    {
		if (!hasTableAccess(UPD
							,CreditReservation_Factory::instance()->className()
							,handle->getUser()))
			return;
		//
    }
	catch (const PS_UserError& e)
    {
		
		WARNING_LOG << e.description()<< std::endl;
		KGL_Response::sendFailure(KNC_FailureCategory::SECURITY, e.description(), handle);
		return;
    }
	catch (const PS_ServerError& e)
    {
		ERROR_LOG << fctName <<": caught exception PS_ServerError, nm=" << (const char*)(e.name);
		ERROR_LOG << ", descr=" << (const char*)(e.description) << ", excpNm" << (const char*)(e.exceptionName()) << endl;
		KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
		return;
    }
	KNDB_LOOP_BEGIN
		try
		{
			//
			KNDB_T_WRITE

				//get the CL source Id from his masterId/timeId
				//sprintf(buffer, "CreditLimitMaster=0x%s and TimeBandId=0x%s",
				//	KNC_ConvId::idToStr((const char*)creditLimitMasterSourceId->getOidVal()).c_str(),
				//	KNC_ConvId::idToStr((const char*)creditTBSourceId->getOidVal()).c_str());

				KGLDB_WhereClause whereClause;
			whereClause.addCondition( "CreditLimitMasterId", "=", creditLimitMasterSourceId );
			whereClause.addCondition( "TimeBandId", "=", creditTBSourceId );

			CreditLimit_Cltn_var CLCltn = CreditLimit_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());
			if(!PS_is_nil(CLCltn) && 0!=CLCltn->length())
			{
				psCreditLimitSource = CLCltn[ 0ul ];
			}
			else
			{
				throw_NOTFOUND(CreditLimit_Factory::instance()->className());
			}

			//get the CL destination Id from his masterId/timeId
			whereClause.erase();
			whereClause.addCondition( "CreditLimitMasterId", "=", creditLimitMasterDestinationId );
			whereClause.addCondition( "TimeBandId", "=", creditTBDestinationId );

			//sprintf(buffer, "CreditLimitMaster=0x%s and TimeBandId=0x%s",
			//	KNC_ConvId::idToStr((const char*)creditLimitMasterDestinationId->getOidVal()).c_str(),
			//	KNC_ConvId::idToStr((const char*)creditTBDestinationId->getOidVal()).c_str());

			CLCltn = CreditLimit_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());
			if(!PS_is_nil(CLCltn) && 0!=CLCltn->length())
			{
				psCreditLimitDestination = CLCltn[ 0ul ];
			}
			else
			{
				throw_NOTFOUND(CreditLimit_Factory::instance()->className());
			}

			PS_Oid_var officeOid;
			PS_Oid_var userOid(new PS_Oid);
			userOid->setOidVal((const unsigned char*)(handle->getUser()).getValue());
			bool status=KNETUserIdToPSOfficeId(handle->getUser(), officeOid);
			//		if(IS_ACCESS_CHANGE())
			{
				if(status &&!CreditLimit_Factory::instance()->hasAccess(false,true,psCreditLimitSource,userOid))
				{
					throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
				}
				if(status &&!PS_is_nil(psCreditLimitSource->arcCreditLimitMaster()->arcCptyCoverage()) &&
				   !Cpty_Factory::instance()->hasAccess(2,false,true,psCreditLimitSource->arcCreditLimitMaster()->arcCptyCoverage(),userOid))
				{
					throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
				}
				if(status &&!PS_is_nil(psCreditLimitSource->arcCreditLimitMaster()->arcFolderCoverage()) &&
				   !Folder_Factory::instance()->hasAccess(2,false,true,psCreditLimitSource->arcCreditLimitMaster()->arcFolderCoverage(),userOid))
				{
					throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
				}
			}


			if(status &&!CreditLimit_Factory::instance()->hasAccess(false,true,psCreditLimitDestination,userOid))
			{
				throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
			}

			if(status &&!PS_is_nil(psCreditLimitDestination->arcCreditLimitMaster()->arcCptyCoverage()) &&
			   !Cpty_Factory::instance()->hasAccess(2,false,true,psCreditLimitDestination->arcCreditLimitMaster()->arcCptyCoverage(),userOid))
			{
				throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
			}
			if(  status &&
				 !PS_is_nil(psCreditLimitDestination->arcCreditLimitMaster()->arcFolderCoverage()) &&
				 !Folder_Factory::instance()->hasAccess(2,false,true,psCreditLimitDestination->arcCreditLimitMaster()->arcFolderCoverage(),userOid))
			{
				throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
			}

			CreditLimitMaster_var psCreditLimitMasterSource = CreditLimitMaster_Factory::instance()->queryKey(*psCreditLimitSource->CreditLimitMasterId(),PS_Defs::k_cacheThenDatabase) ;
			CreditLimitMaster_var psCreditLimitMasterDestination = CreditLimitMaster_Factory::instance()->queryKey(*psCreditLimitDestination->CreditLimitMasterId(),PS_Defs::k_cacheThenDatabase) ;

			if (PS_is_nil(psCreditLimitMasterSource) || PS_is_nil(psCreditLimitMasterDestination))
			{
				KNDB_T_ROLLBACK
					string errMsg(CreditLimit_Factory::instance()->className());
				errMsg+=" destination not found";
				KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
				return;
			}



			//we get the allocatedAmount according to the time band element source
			whereClause.erase();
			whereClause.addCondition( "CreditLimitMasterId", "=", creditLimitMasterSourceId );
			whereClause.addCondition( "TimeBandId", "=", creditTBSourceId );

			TimeBandCoverageElt_Cltn_var collTimeBandElts =	TimeBandCoverageElt_Factory::instance()->querySQLWhere( whereClause.getConditions().c_str() );

			double allocatedAmount = psCreditLimitMasterSource->AllocatedAmount();

			if(collTimeBandElts->length())
			{
				allocatedAmount=collTimeBandElts[(unsigned long)0]->AllocatedAmount();
			}


			if(allocatedAmount < (creditReservationTransfer.getAllocatedAmount() +
					getReservedAmount(psCreditLimitSource, creditReservationSourceId)) )
			{
				KNDB_T_ROLLBACK
					string errMsg(CreditLimit_Factory::instance()->className());
				errMsg+=" reservation amount larger than the limit";
				KGL_Response::sendFailure(KNC_FailureCategory::LOGICAL, errMsg.c_str(), handle);
				return;
			}



			//
			CreditReservation_var toUpdateCreditReservationSource
				= KNCBTK_CoreBasic<CreditReservation_var
				,CreditReservation_Factory>
				::queryId(creditReservationSourceId);

			whereClause.erase();
			whereClause.addCondition( "creditReservationSourceId", "=", creditReservationSourceId );

			TRACE_LOG << whereClause.getConditions().c_str() << endl;

			if (PS_is_nil(toUpdateCreditReservationSource))
			{
				KNDB_T_ROLLBACK
					string errMsg(CreditReservation_Factory::instance()->className());
				errMsg+=" crsource to update not found";
				KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
				return;
			}
			//
			CreditReservation_var toUpdateCreditReservationDestination
				= CreditReservation_Factory::instance()->queryKey(*toUpdateCreditReservationSource->CreditReservationId_Transfer()
																  ,PS_Defs::k_cacheThenDatabase);
			if (PS_is_nil(toUpdateCreditReservationDestination))
			{
				KNDB_T_ROLLBACK
					string errMsg(CreditReservation_Factory::instance()->className());
				errMsg+=" crdestination to update not found";
				KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
				return;
			}
			//
			kncbtkAuditMsg_CreditReservation_.logPreUpdate(toUpdateCreditReservationSource,1);
			kncbtkAuditMsg_CreditReservation2_.logPreUpdate(toUpdateCreditReservationDestination,2);
			KNETToPSCreditReservationTransfer(handle
											  ,psCreditLimitSource
											  ,psCreditLimitDestination
											  ,creditReservationTransfer
											  ,toUpdateCreditReservationSource
											  ,toUpdateCreditReservationDestination);
			KNDB_T_COMMIT
				kncbtkAuditMsg_CreditReservation_.logPostUpdate(handle->getUser()
																,toUpdateCreditReservationSource
																,toUpdateCreditReservationSource->Id(),1);
			kncbtkAuditMsg_CreditReservation2_.logPostUpdate(handle->getUser()
															 ,toUpdateCreditReservationDestination
															 ,toUpdateCreditReservationDestination->Id(),2);

			KNC_Result res = KNET_DataResponse::sendUpdateSuccess( handle );
			if(!res)
			{
				throw_LOGICAL(res.text());
			};

			// Dashboard prepare broadcast
			KNET_CreditReservationTransferAccess knetCreditReservationTransfer;
			PSToKNETCreditReservationTransfer(toUpdateCreditReservationSource, knetCreditReservationTransfer);

			// Send Dashboard broadcast message
			KGL_CreditReservationTransferAdapterImpl UpdatedObject;
			UpdatedObject.setRawData( knetCreditReservationTransfer );
			UpdatedObject.setObjectType(KGLE_AsyncFwkObjectType::CREDITRESERVATIONTRANSFER);
			KGLAF_AsyncFwk::instance().sendNotification(KGLE_AsyncMsgType::UPDATED, UpdatedObject);

			return;
		}
	catch (const PS_ServerError& e)
    {
		KNDB_T_ROLLBACK
			KNC_Result kncResultHE
			= KNDB_HANDLE_EXCEPTION(e);
		if (!kncResultHE)
        {
			ERROR_LOG << e.description << std::endl ;
			//A.G.:DO NOT SEND synchronous message for those treated in asynchronous mode
			//KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
			KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
			return;
        }
    }
	KNDB_LOOP_END
		}
/*
* onRemoveReservationTransfer (KNET_Id...)		!! CreditLimit specific !!
*/
void
KNCB_CreditLimit::onRemoveReservationTransfer (KGR_Id const& creditReservationSourceId,
    KNET_RequestHandle handle)
{
  static const char* fctName = "KNCB_CreditLimit::onRemoveReservationTransfer";
  //
  try
    {
      if (!hasTableAccess(DEL
                          ,CreditReservation_Factory::instance()->className()
                          ,handle->getUser()))
        return;
      //
    }
  catch (const PS_UserError& e)
    {
      
      WARNING_LOG << e.description()<< std::endl;
      KGL_Response::sendFailure(KNC_FailureCategory::SECURITY, e.description(), handle);
      return;
    }
  catch (const PS_ServerError& e)
    {
		ERROR_LOG << fctName <<": caught exception PS_ServerError, nm=" << (const char*)(e.name);
		ERROR_LOG << ", descr=" << (const char*)(e.description) << ", excpNm" << (const char*)(e.exceptionName()) << endl;
      KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
      return;
    }
  KNDB_LOOP_BEGIN
  try
    {
      //
      CreditReservation_var toDeleteCreditReservationSource
      = KNCBTK_CoreBasic<CreditReservation_var
        ,CreditReservation_Factory>
        ::queryId(creditReservationSourceId);
      if (PS_is_nil(toDeleteCreditReservationSource))
        {
          KNDB_T_ROLLBACK
          string errMsg(CreditReservation_Factory::instance()->className());
          errMsg+=" crsource to delete not found";
          KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
          return;
        }

	  // Dashboard prepare broadcast
	  KNET_CreditReservationTransferAccess knetCreditReservationTransfer;
	  PSToKNETCreditReservationTransfer(toDeleteCreditReservationSource, knetCreditReservationTransfer);

      //
      PS_Oid_var officeOid;
      PS_Oid_var userOid(new PS_Oid);
      userOid->setOidVal((const unsigned char*)(handle->getUser()).getValue());
      bool status=KNETUserIdToPSOfficeId(handle->getUser(), officeOid);



      if(status &&!CreditLimit_Factory::instance()->hasAccess(false,true,toDeleteCreditReservationSource->arcCreditLimit(),userOid))
        {
          throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }
      if(status &&!PS_is_nil(toDeleteCreditReservationSource->arcCreditLimit()->arcCreditLimitMaster()->arcCptyCoverage()) &&
          !Cpty_Factory::instance()->hasAccess(2,false,true,toDeleteCreditReservationSource->arcCreditLimit()->arcCreditLimitMaster()->arcCptyCoverage(),userOid))
        {
          throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }
      if(status &&!PS_is_nil(toDeleteCreditReservationSource->arcCreditLimit()->arcCreditLimitMaster()->arcFolderCoverage()) &&
          !Folder_Factory::instance()->hasAccess(2,false,true,toDeleteCreditReservationSource->arcCreditLimit()->arcCreditLimitMaster()->arcFolderCoverage(),userOid))
        {
          throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }

      if(status)
        {
          if(!CreditLimit_Factory::instance()->hasAccess(false,true,toDeleteCreditReservationSource->arcCreditLimitTransfer(),userOid))
            {
              throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
            }
          if(status &&!PS_is_nil(toDeleteCreditReservationSource->arcCreditLimit()->arcCreditLimitMaster()->arcCptyCoverage()) &&
              !Cpty_Factory::instance()->hasAccess(2,false,true,toDeleteCreditReservationSource->arcCreditLimit()->arcCreditLimitMaster()->arcCptyCoverage(),userOid))
            {
              throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
            }
          if(status &&!PS_is_nil(toDeleteCreditReservationSource->arcCreditLimit()->arcCreditLimitMaster()->arcFolderCoverage()) &&
              !Folder_Factory::instance()->hasAccess(2,false,true,toDeleteCreditReservationSource->arcCreditLimit()->arcCreditLimitMaster()->arcFolderCoverage(),userOid))
            {
              throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
            }
        }

      //
      CreditReservation_var toDeleteCreditReservationDestination
      = CreditReservation_Factory::instance()->queryKey(*toDeleteCreditReservationSource->CreditReservationId_Transfer()
          ,PS_Defs::k_cacheThenDatabase);
      if (PS_is_nil(toDeleteCreditReservationDestination))
        {
          KNDB_T_ROLLBACK
          string errMsg(CreditReservation_Factory::instance()->className());
          errMsg+=" crdestination to delete not found";
          KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
          return;
        }
      KNDB_T_WRITE_IMMEDIATE
      //
      //
      kncbtkAuditMsg_CreditReservation_.logPrepareDelete(handle->getUser()
          ,toDeleteCreditReservationSource
          ,toDeleteCreditReservationSource->Id(),1);
      kncbtkAuditMsg_CreditReservation2_.logPrepareDelete(handle->getUser()
          ,toDeleteCreditReservationDestination
          ,toDeleteCreditReservationDestination->Id(),2);
      CreditReservation_Factory::instance()->remove
      (toDeleteCreditReservationSource);

      // this second delete have not to be done because the first one
      // is propagate to it's related data (that one)
      // CreditReservation_Factory::instance()->remove(toDeleteCreditReservationDestination);

      KNDB_T_COMMIT
      kncbtkAuditMsg_CreditReservation_.logCommitDelete(1);
      kncbtkAuditMsg_CreditReservation2_.logCommitDelete(2);

      KNC_Result res = KNET_DataResponse::sendRemoveSuccess( handle );
      if(!res)
        {
          throw_LOGICAL(res.text());
        };

      // Send Dashboard broadcast message
	  KGL_CreditReservationTransferAdapterImpl RemovedObject;
	  RemovedObject.setRawData( knetCreditReservationTransfer );
	  RemovedObject.setObjectType(KGLE_AsyncFwkObjectType::CREDITRESERVATIONTRANSFER);
	  KGLAF_AsyncFwk::instance().sendNotification(KGLE_AsyncMsgType::DELETED, RemovedObject);

      return;
    }
  catch (const PS_ServerError& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
	  //A.G.:DO NOT SEND synchronous message for those treated in asynchronous mode
          //KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
          KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
          return;
        }
    }
  KNDB_LOOP_END
}
/*
* onGetReservationTransfer (KNET_Id...)		!! CreditLimit specific !!
*/
void
KNCB_CreditLimit::onGetReservationTransfer (KGR_Id const& creditLimitSourceId,				//masterId
    KGR_Id const& creditLimitDestinationId,			//masterId
    KGR_Id const& timeBandSourceId,
    KGR_Id const& timeBandDestinationId,
    KNET_RequestHandle handle)
{
	//
	KNDB_LOOP_BEGIN
		try
		{

			CreditLimit_var psCreditLimitSource;
			CreditLimit_var psCreditLimitDestination;
			char buffer[255];
			//get the CL source Id from his masterId/timeId
			//sprintf(buffer, "CreditLimitMaster=0x%s and TimeBandId=0x%s",
			//	KNC_ConvId::idToStr((const char*)creditLimitMasterSourceId->getOidVal()).c_str(),
			//	KNC_ConvId::idToStr((const char*)creditTBSourceId->getOidVal()).c_str());

			KGLDB_WhereClause whereClause;
			whereClause.addCondition( "CreditLimitMasterId", "=", creditLimitSourceId );
			whereClause.addCondition( "TimeBandId", "=", timeBandSourceId );

			//		TRACE_LOG << whereClause.getConditions().c_str() << endl;

			CreditLimit_Cltn_var CLColl = CreditLimit_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());
			if(!PS_is_nil(CLColl) && 0!=CLColl->length())
			{
				psCreditLimitSource = CLColl[ 0ul ];
			}
			else
			{
				throw_NOTFOUND(CreditLimit_Factory::instance()->className());
			}

			//get the CL destination Id from his masterId/timeId
			whereClause.erase();
			whereClause.addCondition( "CreditLimitMasterId", "=", creditLimitDestinationId );
			whereClause.addCondition( "TimeBandId", "=", timeBandDestinationId );

			//sprintf(buffer, "CreditLimitMaster=0x%s and TimeBandId=0x%s",
			//	KNC_ConvId::idToStr((const char*)creditLimitMasterDestinationId->getOidVal()).c_str(),
			//	KNC_ConvId::idToStr((const char*)creditTBDestinationId->getOidVal()).c_str());

			//		TRACE_LOG << whereClause.getConditions().c_str() << endl;

			CLColl = CreditLimit_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());
			if(!PS_is_nil(CLColl) && 0!=CLColl->length())
			{
				psCreditLimitDestination = CLColl[ 0ul ];
			}
			else
			{
				throw_NOTFOUND(CreditLimit_Factory::instance()->className());
			}


			//get the reservation 'destination' (for the right amount)
			sprintf(buffer, "CreditLimitId=0x%s and CreditLimitId_Transfer=0x%s and CreditReservationId_Transfer is not NULL",
					KNC_ConvId::idToStr((const char*)psCreditLimitSource->Id()->getOidVal()).c_str(),
					KNC_ConvId::idToStr((const char*)psCreditLimitDestination->Id()->getOidVal()).c_str());

			CreditReservation_Cltn_var coll = CreditReservation_Factory::instance()->querySQLWhere(buffer);
			if (PS_is_nil(coll) ||  0==coll->length() )
			{
				KNDB_T_ROLLBACK
					string errMsg(CreditReservation_Factory::instance()->className());
				errMsg+="Transfer not found";
				KGL_Response::sendFailure(KNC_FailureCategory::LOGICAL, errMsg.c_str(), handle);
				return;
			}
			//
			KNDB_T_READ

				KNCB_CreditLimit::RELATED_PS_CLASS_VAR psCreditLimitSource1 =
				KNCBTK_CoreBasic< KNCB_CreditLimit::RELATED_PS_CLASS_VAR,
				KNCB_CreditLimit::RELATED_PS_FACTORY>
				::queryId(creditLimitSourceId);

			if (PS_is_nil(psCreditLimitSource1))
			{
				KNDB_T_ROLLBACK
					string errMsg(KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->className());
				errMsg+=" source not found";
				KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
				return;
			}
			PS_Oid_var officeOid;
			PS_Oid_var userOid(new PS_Oid);
			userOid->setOidVal((const unsigned char*)(handle->getUser()).getValue());
			bool status=KNETUserIdToPSOfficeId(handle->getUser(), officeOid);
			if(!KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->hasAccess(true,false,psCreditLimitSource1,userOid))
			{
				throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
			}
			if(!PS_is_nil(psCreditLimitSource1->arcCptyCoverage()) &&
			   !Cpty_Factory::instance()->hasAccess(2,true,false,psCreditLimitSource1->arcCptyCoverage(),userOid))
			{
				throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
			}
			if(!PS_is_nil(psCreditLimitSource1->arcFolderCoverage()) &&
			   !Folder_Factory::instance()->hasAccess(2,true,false,psCreditLimitSource1->arcFolderCoverage(),userOid))
			{
				throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
			}

			KNCB_CreditLimit::RELATED_PS_CLASS_VAR psCreditLimitDestination1 =
				KNCBTK_CoreBasic< KNCB_CreditLimit::RELATED_PS_CLASS_VAR,
				KNCB_CreditLimit::RELATED_PS_FACTORY >
				::queryId(creditLimitDestinationId);

			if (PS_is_nil(psCreditLimitDestination1))
			{
				KNDB_T_ROLLBACK
					string errMsg(KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->className());
				errMsg+=" destination not found";
				KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
				return;
			}
			if(!KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->hasAccess(true,false,psCreditLimitDestination1,userOid))
			{
				throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
			}
			if(status &&!PS_is_nil(psCreditLimitDestination1->arcCptyCoverage()) &&
			   !Cpty_Factory::instance()->hasAccess(2,true,false,psCreditLimitDestination1->arcCptyCoverage(),userOid))
			{
				throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
			}
			if(status &&!PS_is_nil(psCreditLimitDestination1->arcFolderCoverage()) &&
			   !Folder_Factory::instance()->hasAccess(2,true,false,psCreditLimitDestination1->arcFolderCoverage(),userOid))
			{
				throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
			}

			//!!
			// Qu'est-ce qui interdit d'avoir plusieurs CreditReservations
			// avec les m???mes CreditLimitId et CreditLimitId_Transfer ?
			// => Qu'est-ce qui garantit qu'il n'y aura au plus
			// qu'un seul r???sultat??
			// en fait c le gui qui fait un get avant l'insert.
			// mais en jouant avec l'api on peut en inserer plusieurs...
			//!!
			KNET_CreditReservationTransferAccess knetCreditReservationTransfer;
			PSToKNETCreditReservationTransfer(coll[0ul], knetCreditReservationTransfer);
			KNDB_T_COMMIT
				KNC_Result res=KNCB_CreditLimit::RELATED_VALIDATION_RESPONSE_CLASS::sendGetReservationTransferSuccess(knetCreditReservationTransfer
																													  ,handle);
			if(!res)
			{
				throw_LOGICAL(res.text());
			};
			return;
		}
	catch (const PS_ServerError& e)
    {
		KNDB_T_ROLLBACK
			KNC_Result kncResultHE
			= KNDB_HANDLE_EXCEPTION(e);
		if (!kncResultHE)
        {
			ERROR_LOG << e.description << std::endl ;
			KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
			return;
        }
    }
	KNDB_LOOP_END
		}
/*
* onQueryAllReservation (KNET_RequestHandle handle)		!! CreditLimit specific !!
*/
void
KNCB_CreditLimit::onQueryAllReservation (KNET_RequestHandle handle)
{
  //
  KNDB_LOOP_BEGIN
  try
    {
      PS_Oid_var userOid(new PS_Oid);
      userOid->setOidVal((const unsigned char*)(handle->getUser()).getValue());
      KGLDB_WhereClause whereClause;
      whereClause.addExpression("CreditLimitId_Transfer is NULL");
      whereClause.addExpression("AND CreditReservationId_Transfer is NULL");
      //
      KGR_Collection<KNET_CreditReservationAccess> creditReservationCollection;
      //
      KNDB_T_READ
      CreditReservation_Cltn_var cltn
      = CreditReservation_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());
      unsigned long totalCount=cltn->length();
      //
      if (totalCount==0)
        {
          KNDB_T_ROLLBACK
          string errMsg(CreditReservation_Factory::instance()->className());
          errMsg+=" not found";
          KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND
                                    ,errMsg.c_str()
                                    ,handle);
          return;
        }
      unsigned long i= (unsigned long) 0.0;
      PS_Oid_var officeOid;
      bool status=KNETUserIdToPSOfficeId(handle->getUser(), officeOid);
      for (;i<totalCount;++i)
        {

          KNET_CreditReservationAccess knetCreditReservation;
          if(   !PS_is_nil(cltn[i]->arcCreditLimit()) &&
          	!CreditLimit_Factory::instance()->hasAccess(true,false,cltn[i]->arcCreditLimit(),userOid))
            continue;

          if(   !PS_is_nil(cltn[i]->arcCreditLimitTransfer()) &&
          	!CreditLimit_Factory::instance()->hasAccess(true,false,cltn[i]->arcCreditLimitTransfer(),userOid))
            continue;

          if(status &&
          	!PS_is_nil(cltn[i]->arcCreditLimit()->arcCreditLimitMaster()) &&
          	!PS_is_nil(cltn[i]->arcCreditLimit()->arcCreditLimitMaster()->arcCptyCoverage()) &&
              !Cpty_Factory::instance()->hasAccess(2,true,false,cltn[i]->arcCreditLimit()->arcCreditLimitMaster()->arcCptyCoverage(),userOid))
            {
              //throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
              //No access
              continue;

            }
          if(  status &&
              !PS_is_nil(cltn[i]->arcCreditLimit()->arcCreditLimitMaster()->arcFolderCoverage()) &&
              !Folder_Factory::instance()->hasAccess(2,true,false,cltn[i]->arcCreditLimit()->arcCreditLimitMaster()->arcFolderCoverage(),userOid))
            {
              //throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
              //No access
              continue;
            }

          
          PSToKNETCreditReservation(cltn[(unsigned long) i], knetCreditReservation);


          //			if(IS_ACCESS_ACCESS())
          // 			{
          // 				if(status)
          // 				{
          // 					//TOTOF SEE CREDIT COVERAGE TEST
          // 					bool s=true;
          // 					if(!cltn[i]->CptyId_CoverageNULL())
          // 					{
          // 						if(!Cpty_Factory::instance()->hasAccess(cltn[i]->arcCpty(),officeOid))
          // 							s = false;
          // 					}

          // 					if(!cltn[i]->FolderId_CoverageNULL())
          // 					{
          // 						if(!Folder_Factory::instance()->hasAccess(cltn[i]->arcFolder(),officeOid))
          // 							s = false;
          // 					}
          // 					if(!cltn[i]->InstrumentId_CoverageNULL())
          // 					{
          // 						if(!Instrument_Factory::instance()->hasAccess(cltn[i]->arcInstrument(),officeOid))
          // 							s = false;
          // 					}
          // 					if(!KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->hasAccess(cltn[i]->arcCreditLimit(),officeOid))
          // 						s = false;
          // 					if(!cltn[i]->arcCreditLimit()->CptyId_CoverageNULL())
          // 					{
          // 						if(!Cpty_Factory::instance()->hasAccess(cltn[i]->arcCreditLimit()->arcCptyCoverage(),officeOid))
          // 							s = false;
          // 					}

          // 					if(!cltn[i]->arcCreditLimit()->FolderId_CoverageNULL())
          // 					{
          // 						if(!Folder_Factory::instance()->hasAccess(cltn[i]->arcCreditLimit()->arcFolderCoverage(),officeOid))
          // 							s = false;
          // 					}
          // 					if(s)
          // 						creditReservationCollection.push_back(knetCreditReservation);
          // 				}
          // 				else
          TODO("begin 004");
          creditReservationCollection.push_back(knetCreditReservation);
          TODO("end 004");
          //			}
          // 			else
          // 			{
          // 					creditReservationCollection.push_back(knetCreditReservation);
          // 			}
        }
      KNDB_T_COMMIT
      //
      KNC_Result res
      = KNCB_CreditLimit::RELATED_VALIDATION_RESPONSE_CLASS::sendQueryAllReservationSuccess(creditReservationCollection
          ,handle);
      if(!res)
        {
          throw_LOGICAL(res.text());
        };
    }
  catch(PS_ServerError const& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
          KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
          return;
        }
    }
  KNDB_LOOP_END
}

/*
 * onQueryAllReservationTransfer (KNET_RequestHandle handle)		!! CreditLimit specific !!
 */
void
KNCB_CreditLimit::onQueryAllReservationTransfer (KNET_RequestHandle handle)
{
  //
  KNDB_LOOP_BEGIN
  try
    {
      PS_Oid_var userOid(new PS_Oid);
      userOid->setOidVal((const unsigned char*)(handle->getUser()).getValue());
      KGLDB_WhereClause whereClause;
      // be careful, reservation source transfer allocated amounts
      // are in currency of the source Limit
      whereClause.addExpression("CreditLimitId_Transfer is not NULL");
      whereClause.addExpression("AND CreditReservationId_Transfer is not NULL");
      whereClause.addExpression("AND AllocatedAmount>=0");
      //
      KGR_Collection<KNET_CreditReservationTransferAccess> creditReservationTransferCollection;
      //
      KNDB_T_READ
      CreditReservation_Cltn_var cltn
      = CreditReservation_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());
      unsigned long totalCount=cltn->length();
      //
      if (totalCount==0)
        {
          KNDB_T_ROLLBACK
          //string errMsg(CreditReservation_Factory::instance()->className());
          string errMsg("CreditReservationTransfer");
          errMsg+=" not found";
          KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND
                                    ,errMsg.c_str()
                                    ,handle);
          return;
        }

      unsigned long  i= (unsigned long) 0.0;
      PS_Oid_var officeOid;
      bool status=KNETUserIdToPSOfficeId(handle->getUser(), officeOid);
      for (;i<totalCount;++i)
        {
          KNET_CreditReservationTransferAccess knetCreditReservationTransfer;
          
          TODO("begin 004");

          if( !PS_is_nil(cltn[i]->arcCreditLimit()) &&
              !CreditLimit_Factory::instance()->hasAccess(true,false,cltn[i]->arcCreditLimit(),userOid))
            continue;

          if( !PS_is_nil(cltn[i]->arcCreditLimitTransfer()) &&
              !CreditLimit_Factory::instance()->hasAccess(true,false,cltn[i]->arcCreditLimitTransfer(),userOid))
            continue;

          if(status &&
              !PS_is_nil(cltn[i]->arcCreditLimit()->arcCreditLimitMaster()) &&
              !PS_is_nil(cltn[i]->arcCreditLimit()->arcCreditLimitMaster()->arcCptyCoverage()) &&
              !Cpty_Factory::instance()->hasAccess(2,true,false,cltn[i]->arcCreditLimit()->arcCreditLimitMaster()->arcCptyCoverage(),userOid))
            continue;

          if(status &&!PS_is_nil(cltn[i]->arcCreditLimit()->arcCreditLimitMaster()->arcFolderCoverage()) &&
              !Folder_Factory::instance()->hasAccess(2,true,false,cltn[i]->arcCreditLimit()->arcCreditLimitMaster()->arcFolderCoverage(),userOid))
            continue;


          if(status &&
              !PS_is_nil(cltn[i]->arcCreditLimitTransfer()->arcCreditLimitMaster()) &&
              !PS_is_nil(cltn[i]->arcCreditLimitTransfer()->arcCreditLimitMaster()->arcCptyCoverage()) &&
              !Cpty_Factory::instance()->hasAccess(2,true,false,cltn[i]->arcCreditLimitTransfer()->arcCreditLimitMaster()->arcCptyCoverage(),userOid))
            continue;

          if(status &&!PS_is_nil(cltn[i]->arcCreditLimitTransfer()->arcCreditLimitMaster()->arcFolderCoverage()) &&
              !Folder_Factory::instance()->hasAccess(2,true,false,cltn[i]->arcCreditLimitTransfer()->arcCreditLimitMaster()->arcFolderCoverage(),userOid))
            continue;


          PSToKNETCreditReservationTransfer(cltn[(unsigned long) i], knetCreditReservationTransfer);
          TODO("end 004");

          //			if(IS_ACCESS_ACCESS())
          // 			{
          // 				if(status)
          // 				{
          // 					//TOTOF SEE CREDIT COVERAGE TEST
          // 					bool s=true;
          // 					if(!cltn[i]->CptyId_CoverageNULL())
          // 					{
          // 						if(!Cpty_Factory::instance()->hasAccess(cltn[i]->arcCpty(),officeOid))
          // 							s = false;
          // 					}

          // 					if(!cltn[i]->FolderId_CoverageNULL())
          // 					{
          // 						if(!Folder_Factory::instance()->hasAccess(cltn[i]->arcFolder(),officeOid))
          // 							s = false;
          // 					}
          // 					if(!cltn[i]->InstrumentId_CoverageNULL())
          // 					{
          // 						if(!Instrument_Factory::instance()->hasAccess(cltn[i]->arcInstrument(),officeOid))
          // 							s = false;
          // 					}
          // 					if(!KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->hasAccess(cltn[i]->arcCreditLimit(),officeOid))
          // 						s = false;
          // 					if(!KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->hasAccess(cltn[i]->arcCreditLimitTransfer(),officeOid))
          // 						s = false;
          // 					if(!cltn[i]->arcCreditLimit()->CptyId_CoverageNULL())
          // 					{
          // 						if(!Cpty_Factory::instance()->hasAccess(cltn[i]->arcCreditLimit()->arcCptyCoverage(),officeOid))
          // 							s = false;
          // 					}

          // 					if(!cltn[i]->arcCreditLimit()->FolderId_CoverageNULL())
          // 					{
          // 						if(!Folder_Factory::instance()->hasAccess(cltn[i]->arcCreditLimit()->arcFolderCoverage(),officeOid))
          // 							s = false;
          // 					}
          // 					if(s)
          // 						creditReservationTransferCollection.push_back(knetCreditReservationTransfer);


          // 				}
          // 				else
          creditReservationTransferCollection.push_back(knetCreditReservationTransfer);
          //			}
          // 			else
          // 			{
          // 					creditReservationTransferCollection.push_back(knetCreditReservationTransfer);

          // 			}
        }
      KNDB_T_COMMIT
      //
      KNC_Result res
      = KNCB_CreditLimit::RELATED_VALIDATION_RESPONSE_CLASS::sendQueryAllReservationTransferSuccess(creditReservationTransferCollection
          ,handle);
      if(!res)
        {
          throw_LOGICAL(res.text());
        };
    }
  catch(PS_ServerError const& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
          KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
          return;
        }
    }
  KNDB_LOOP_END
}

/*
 * onQueryReservationTransfer (KNET_RequestHandle handle)		!! CreditLimit specific !!
 *
 * same code as onQueryAllReservationTransfer + filter on fromDate
 */
void
KNCB_CreditLimit::onQueryReservationTransfer (  KGR_Id const& userId,
    											KNET_RequestHandle handle,
    											char const * responseInbox )
{
	static const char* fctName = "KNCB_CreditLimit::onQueryReservationTransfer";
  //
  KNDB_LOOP_BEGIN
  try
    {
	  string strResponseInbox(responseInbox);

	  KNUserConfig_var userConfig =
				KNCBTK_CoreBasic<KNUserConfig_var,KNUserConfig_Factory>::queryId(userId);

	  int horizon;
	  if (PS_is_nil(userConfig))
		horizon = 1;
	  else
		horizon = (*userConfig).DashboardHistoryDays();

	  // find nNbrDays = the number of dates
	  int nNbrDays = 0;
	  KNC_Date Today;
	  KNC_Date kncFromDate;
	  KNCB_Calendar* pInstance = KNCB_Calendar::instance();
	  Today.Now();
	  KGR_Id CurrencyId((*userConfig).DashboardCurrencyId()->getOidVal());

	  pInstance->previousBusinessDay(CurrencyId,
									 Today,
									 kncFromDate,
									 nNbrDays,
									 horizon);

	  // find corresponding dates
	  KGR_Date kgrFromDate;
	  kgrFromDate.setDate(kncFromDate);

      PS_Oid_var userOid(new PS_Oid);
      userOid->setOidVal((const unsigned char*)(handle->getUser()).getValue());

	  ostringstream myStream1, myStream2, myStream3;

	  myStream1 << kgrFromDate.getMonth() << flush;
      string strFromDate(myStream1.str());

      myStream2 << kgrFromDate.getDay() << flush;
      strFromDate = strFromDate + "/" + myStream2.str();

      myStream3 << kgrFromDate.getYear() << flush;
      strFromDate = strFromDate + "/" + myStream3.str();

      KGLDB_WhereClause whereClause;
      // be careful, reservation source transfer allocated amounts
      // are in currency of the source Limit
      whereClause.addExpression("CreditLimitId_Transfer is not NULL");
      whereClause.addExpression("AND CreditReservationId_Transfer is not NULL");
      whereClause.addExpression("AND AllocatedAmount>=0");
      whereClause.addExpression("AND ( EndDate IS NULL OR EndDate > '");
      whereClause.addExpression(strFromDate.c_str());
      whereClause.addExpression("' )");
      whereClause.addExpression("AND ( BeginDate IS NULL OR BeginDate <= '");
      whereClause.addExpression(KNC_ConvDate::longToStr(KNC_ConvDate::getNow()).c_str());
      whereClause.addExpression("' )");
      //
      vector<KNET_CreditReservationTransferAccess> creditReservationTransferCollection;
      //KGR_Collection<KNET_CreditReservationTransferAccess> creditReservationTransferCollection;

      //
      KNDB_T_READ
      CreditReservation_Cltn_var cltn
      = CreditReservation_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());
      unsigned long totalCount=cltn->length();
      //
      if (totalCount==0)
        {
          KNDB_T_ROLLBACK
          //string errMsg(CreditReservation_Factory::instance()->className());
          string errMsg("CreditReservationTransfer");
          errMsg+=" not found";
          //KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND
	  //                         ,errMsg.c_str()
	  //                        ,handle);
          return;
        }

      unsigned long  i= (unsigned long) 0.0;
      PS_Oid_var officeOid;

      bool status=KNETUserIdToPSOfficeId(handle->getUser(), officeOid);

      for (;i<totalCount;++i)
        {
          KNET_CreditReservationTransferAccess knetCreditReservationTransfer;

          if( !PS_is_nil(cltn[i]->arcCreditLimit()) &&
              !CreditLimit_Factory::instance()->hasAccess(true,false,cltn[i]->arcCreditLimit(),userOid))
            continue;
          if( !PS_is_nil(cltn[i]->arcCreditLimitTransfer()) &&
              !CreditLimit_Factory::instance()->hasAccess(true,false,cltn[i]->arcCreditLimitTransfer(),userOid))
            continue;

		  Cpty_var cptyCov;
		  if(!PS_is_nil(cltn[i]->arcCreditLimit()->arcCreditLimitMaster()) )
			  cptyCov = cltn[i]->arcCreditLimit()->arcCreditLimitMaster()->arcCptyCoverage();
          if(status &&
			 !PS_is_nil(cptyCov) &&
			 !Cpty_Factory::instance()->hasAccess(2,true,false,cptyCov,userOid) )
            continue;

		  Folder_var folderCov;
		  if(!PS_is_nil(cltn[i]->arcCreditLimit()->arcCreditLimitMaster()) )
			  folderCov = cltn[i]->arcCreditLimit()->arcCreditLimitMaster()->arcFolderCoverage();
          if(status &&
			 !PS_is_nil(folderCov) &&
              !Folder_Factory::instance()->hasAccess(2,true,false,folderCov,userOid))
            continue;

		  Cpty_var transferCptyCov;
		  if(!PS_is_nil(cltn[i]->arcCreditLimitTransfer()->arcCreditLimitMaster()) )
			  transferCptyCov = cltn[i]->arcCreditLimitTransfer()->arcCreditLimitMaster()->arcCptyCoverage();
          if(status &&
			 !PS_is_nil(transferCptyCov) &&
			 !Cpty_Factory::instance()->hasAccess(2,true,false,transferCptyCov,userOid)
              )
            continue;

 		  Folder_var transferFolderCov;
		  if(!PS_is_nil(cltn[i]->arcCreditLimitTransfer()->arcCreditLimitMaster()) )
			  transferFolderCov = cltn[i]->arcCreditLimitTransfer()->arcCreditLimitMaster()->arcFolderCoverage();
         if(status &&
			!PS_is_nil(transferFolderCov) &&
			!Folder_Factory::instance()->hasAccess(2,true,false,transferFolderCov,userOid)
              )
            continue;


          PSToKNETCreditReservationTransfer(cltn[(unsigned long) i], knetCreditReservationTransfer);

          creditReservationTransferCollection.push_back(knetCreditReservationTransfer);
        }
      KNDB_T_COMMIT
      //
	  KGL_CreditReservationTransferAdapterVectorImpl ResponseListObject;
	  ResponseListObject.setRawData( creditReservationTransferCollection );
	  ResponseListObject.setObjectType(KGLE_AsyncFwkObjectType::CREDITRESERVATIONTRANSFER);
	  KGLAF_AsyncFwk::instance().sendNotification(KGLE_AsyncMsgType::INSERTED,
															ResponseListObject,
															&strResponseInbox);
  	  //KNC_Result res
      //= KNCB_CreditLimit::RELATED_VALIDATION_RESPONSE_CLASS::sendQueryReservationTransferSuccess(creditReservationTransferCollection
      //    ,handle);
      //if(!res)
      //  {
      //    throw_LOGICAL(res.text());
      //  };
    }
  catch(PS_ServerError const& e)
    {
		cerr << fctName << " " << e.description << endl;
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
	  //A.G.:DO NOT SEND synchronous message for those treated in asynchronous mode
          //KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
          return;
        }
    }
  KNDB_LOOP_END
}

/*
 * onGetHistorisationCurves()
 */
void
KNCB_CreditLimit::onGetHistorisationCurves( char const *coverageShortName,
    char const *riskWeightCoverageShortName,
    char const *timebandShortName,
    KNET_CreditLimitRequestCB::SovereignKind sovereignKind,
    KNET_Limit::LimitKind limitKind,
    char const *cptyName,
    char const *capCptyName,
    KNET_CreditLimitRequestCB::RefModeIG cptyRefMode,
    char const *folderShortName,
    KNET_CreditLimitRequestCB::RefMode folderRefMode,
    char const *countryShortName,
    KNET_CreditLimitRequestCB::RefMode countryRefMode,
    char const *industryShortName,
    KNET_CreditLimitRequestCB::RefMode industryRefMode,
    char const *currencyShortName,
    KNET_CreditLimitRequestCB::RefMode currencyRefMode,
    char const *userShortName,
    KNET_CreditLimitRequestCB::RefMode userRefMode,
    char const *ratingAgencyShortName,
    char const *ratingShortName,
    KGR_Date const & horizonDate,
    KNET_RequestHandle handle )
{
  // todo status
  // StoreProcedure parameters
  char sovereignKindChar   = *KNETToPSSovereignKind(sovereignKind).c_str();
  char limitKindChar       = *KNETToPSLimitKind(limitKind).c_str();
  char cptyRefModeChar     = *KNETToPSRefModeIG(cptyRefMode).c_str();
  char folderRefModeChar   = *KNETToPSRefMode(folderRefMode).c_str();
  char countryRefModeChar  = *KNETToPSRefMode(countryRefMode).c_str();
  char industryRefModeChar = *KNETToPSRefMode(industryRefMode).c_str();
  char currencyRefModeChar = *KNETToPSRefMode(currencyRefMode).c_str();
  char userRefModeChar     = *KNETToPSRefMode(userRefMode).c_str();

  char coverage[16+1];
  char rwc[16+1];
  char timeband[16+1];
  char cpty[50+1];
  char capCpty[50+1];
  char folder[16+1];
  char country[16+1];
  char industry[16+1];
  char currency[16+1];
  char user[16+1];
  char ratingAgency[16+1];
  char rating[16+1];

  snprintf(coverage,16+1,"%s",coverageShortName);
  snprintf(rwc,16+1,"%s",riskWeightCoverageShortName);
  snprintf(timeband,16+1,"%s",timebandShortName);
  snprintf(cpty,50+1,"%s",cptyName);
  snprintf(capCpty,50+1,"%s",capCptyName);
  snprintf(folder,16+1,"%s",folderShortName);
  snprintf(country,16+1,"%s",countryShortName);
  snprintf(industry,16+1,"%s",industryShortName);
  snprintf(currency,16+1,"%s",currencyShortName);
  snprintf(user,16+1,"%s",userShortName);
  snprintf(ratingAgency,16+1,"%s",ratingAgencyShortName);
  snprintf(rating,16+1,"%s",ratingShortName);

  // bindingParams


  // IDA initialisation
  KT_PtrWrapper< KDBT_DBEnv >             envIDA(new KDBT_DBEnv(serverParams_));
  KT_PtrWrapper< K_CallableStatement_ac > stmt( envIDA->getClbStmt() );

  	KGLB_Date kglbDate(horizonDate.getDate().getYear(),
					horizonDate.getDate().getMonth(),
					horizonDate.getDate().getDay());


  stmt->freeStmt();
  stmt->Prepare( "FetchCreditLimitHistorical" );
  stmt->BindParam_string(  1, coverage, 16+1 );
  stmt->BindParam_string(  1, rwc, 16+1 );
  stmt->BindParam_string(  2, timeband, 16+1 );
  stmt->BindParam_char  (  3, &sovereignKindChar );
  stmt->BindParam_char  (  4, &limitKindChar );
  stmt->BindParam_char  (  5, &cptyRefModeChar );
  stmt->BindParam_char  (  6, &folderRefModeChar );
  stmt->BindParam_char  (  7, &countryRefModeChar );
  stmt->BindParam_char  (  8, &industryRefModeChar );
  stmt->BindParam_char  (  9, &currencyRefModeChar );
  stmt->BindParam_char  ( 10, &userRefModeChar );
  stmt->BindParam_string( 11, cpty, 50+1 );
  stmt->BindParam_string( 12, capCpty, 50+1 );
  stmt->BindParam_string( 13, folder, 16+1 );
  stmt->BindParam_string( 14, country, 16+1 );
  stmt->BindParam_string( 15, industry, 16+1 );
  stmt->BindParam_string( 16, currency, 16+1 );
  stmt->BindParam_string( 17, user, 16+1 );
  stmt->BindParam_string( 18, ratingAgency, 16+1 );
  stmt->BindParam_string( 19, rating, 16+1 );
  stmt->BindParam_string( 20, std_const_cast(char *) (kglbDate.toStringDatabaseFormat112().c_str()), 10+1/*horizonDate.getDate().getTimeStr(tmp), 20+1*/ );


  // return params
  int returnStatus = 0;
  int execRes      = 0;


  // the KNETData we want to fill
  KGR_Collection<KNET_LimitUseCurves> toSend;

  // handle result
  if( (execRes = stmt->Exec()) != K_DBDef_ac::DB_SUCCESS )
    {
      KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM,
                                "Couldn't execute FetchCreditLimitHistorical store procedure.",
                                handle);
    }
  else
    {
      while( stmt->MoreResult() == K_DBDef_ac::DB_SUCCESS )
        {
          int resType;
          switch( resType = stmt->getResultType() )
            {
            case K_DBDef_ac::STATUS :
              {
                int i = 1;
                stmt->BindCol_int(&i, &returnStatus);
                while( stmt->Fetch() == K_DBDef_ac::DB_SUCCESS )
                {}

                break;
              }
            case K_DBDef_ac::ROWS :
              {
                int bindRes = 0;
                int dummy = 1;

                date_t histoDate;
                double allocated;
                double used;
                double addOn;
                int    dealCount;

                KGR_Collection<double> usedAmounts;
                KGR_Collection<double> availableAmounts;
                KGR_Collection<double> allocationAmounts;
                KGR_Collection<KGR_Date> histoDates;
                KGR_Collection<int>    dealNbr;

                bindRes = stmt->BindCol_date( &dummy, &histoDate );
                if( bindRes == K_DBDef_ac::DB_SUCCESS )
                  bindRes = stmt->BindCol_double( &dummy, &allocated );
                if( bindRes == K_DBDef_ac::DB_SUCCESS )
                  bindRes = stmt->BindCol_double( &dummy, &used );
                if( bindRes == K_DBDef_ac::DB_SUCCESS )
                  bindRes = stmt->BindCol_double( &dummy, &addOn );
                if( bindRes == K_DBDef_ac::DB_SUCCESS )
                  bindRes = stmt->BindCol_int( &dummy, &dealCount );

                if( bindRes == K_DBDef_ac::DB_SUCCESS )
                  {
                    while( stmt->Fetch() == K_DBDef_ac::DB_SUCCESS )
                      {
                        /* be careful, KNC_Date::getTime_t() truncates dates before 1/1/1970 on winnt */
                        KGR_Date histoDateKnc;
                        histoDateKnc.setDate( KNC_Date(histoDate ));
                        histoDates.push_back( histoDateKnc );
                        dealNbr.push_back( dealCount );
                        usedAmounts.push_back( used );
                        availableAmounts.push_back( addOn );
                        allocationAmounts.push_back( allocated );
                      }


                    unsigned long i;
                    for (i=0;i<histoDates.size() ;i++)
                      {
                        KNET_LimitUseCurves curve(i,
                                                  usedAmounts[i],
                                                  availableAmounts[i],
                                                  allocationAmounts[i],
                                                  dealNbr[i],
                                                  histoDates[i]);
                        toSend.push_back( curve );
                      }


                  }
                else
                  {
                    KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM,
                                              "Couldn't fetch FetchCreditLimitHistorical stored procedure datas",
                                              handle);
                  }
                break;
              }
            default:
              {
                ERROR_LOG << "Unhandled IDA result type : " << resType << endl;
                break;
              }
            }
        }
    }

  if( returnStatus == 0 )
    {
      KNC_Result res=KNCB_CreditLimit::RELATED_VALIDATION_RESPONSE_CLASS::sendGetHistorisationCurvesSuccess( toSend,
                     handle );
      if(!res)
        {
          throw_LOGICAL(res.text());
        };
    }
  else if( returnStatus == 1 )
      {

	  KGL_Response::sendFailure(KNC_FailureCategory::LOGICAL,
	                                 "no limits are found by the stored procedure  FetchCreditLimitHistorical ",
	                                 handle);



      }

  else
    {
	  KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM,
		                                 "FetchCreditLimitHistorical stored procedure call didn't complete properly.",
		                                 handle);
    }
}


void
KNCB_CreditLimit::onGetByNameHistorisationCurves( KNET_Limit::LimitKind limitKind,
    char const *nameCL,
    char const *timebandShortName,
    KGR_Date const & horizonDate,
    KNET_RequestHandle handle )
{
  // todo status
  // StoreProcedure parameters
  char limitKindChar       = *KNETToPSLimitKind(limitKind).c_str();

  char name[40+1];
  char timeband[16+1];

  snprintf(name,16+1,"%s",nameCL);
  snprintf(timeband,16+1,"%s",timebandShortName);

  // bindingParams


  // IDA initialisation
  KT_PtrWrapper< KDBT_DBEnv >             envIDA(new KDBT_DBEnv(serverParams_));
  KT_PtrWrapper< K_CallableStatement_ac > stmt( envIDA->getClbStmt() );

	KGLB_Date kglbDate(horizonDate.getDate().getYear(),
				horizonDate.getDate().getMonth(),
				horizonDate.getDate().getDay());

  stmt->freeStmt();
  stmt->Prepare( "FetchCreditLimitHistoName" );
  stmt->BindParam_char  (  1, &limitKindChar );
  stmt->BindParam_string(  2, name, 16+1 );
  stmt->BindParam_string(  3, timeband, 16+1 );
  stmt->BindParam_string(  4, std_const_cast(char *) (kglbDate.toStringDatabaseFormat112().c_str()), 10+1/*horizonDate.getDate().getTimeStr(tmp), 20+1 */);


  // return params
  int returnStatus = 0;
  int execRes      = 0;


  // the KNETData we want to fill
  KGR_Collection<KNET_LimitUseCurves> toSend;

  // handle result
  if( (execRes = stmt->Exec()) != K_DBDef_ac::DB_SUCCESS )
    {
      KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM,
                                "Couldn't execute FetchCreditLimitHistorical store procedure.",
                                handle);
    }
  else
    {
      while( stmt->MoreResult() == K_DBDef_ac::DB_SUCCESS )
        {
          int resType;
          switch( resType = stmt->getResultType() )
            {
            case K_DBDef_ac::STATUS :
              {
                int i = 1;
                stmt->BindCol_int(&i, &returnStatus);
                while( stmt->Fetch() == K_DBDef_ac::DB_SUCCESS )
                {}

                break;
              }
            case K_DBDef_ac::ROWS :
              {
                int bindRes = 0;
                int dummy = 1;

                date_t histoDate;
                double allocated;
                double used;
                double addOn;
                int    dealCount;

                KGR_Collection<double> usedAmounts;
                KGR_Collection<double> availableAmounts;
                KGR_Collection<double> allocationAmounts;
                KGR_Collection<KGR_Date> histoDates;
                KGR_Collection<int>    dealNbr;

                bindRes = stmt->BindCol_date( &dummy, &histoDate );
                if( bindRes == K_DBDef_ac::DB_SUCCESS )
                  bindRes = stmt->BindCol_double( &dummy, &allocated );
                if( bindRes == K_DBDef_ac::DB_SUCCESS )
                  bindRes = stmt->BindCol_double( &dummy, &used );
                if( bindRes == K_DBDef_ac::DB_SUCCESS )
                  bindRes = stmt->BindCol_double( &dummy, &addOn );
                if( bindRes == K_DBDef_ac::DB_SUCCESS )
                  bindRes = stmt->BindCol_int( &dummy, &dealCount );

                if( bindRes == K_DBDef_ac::DB_SUCCESS )
                  {
                    while( stmt->Fetch() == K_DBDef_ac::DB_SUCCESS )
                      {
                        /* be careful, KNC_Date::getTime_t() truncates dates before 1/1/1970 on winnt */
                        KGR_Date histoDateKnc;
                        histoDateKnc.setDate( KNC_Date(histoDate ));
                        histoDates.push_back( histoDateKnc );
                        dealNbr.push_back( dealCount );
                        usedAmounts.push_back( used );
                        availableAmounts.push_back( addOn );
                        allocationAmounts.push_back( allocated );
                      }

                    unsigned long i;
                    for (i=0;i<histoDates.size() ;i++)
                      {
                        KNET_LimitUseCurves curve(i,
                                                  usedAmounts[i],
                                                  availableAmounts[i],
                                                  allocationAmounts[i],
                                                  dealNbr[i],
                                                  histoDates[i]);
                        toSend.push_back( curve );
                      }
                  }
                else
                  {
                    KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM,
                                              "Couldn't fetch FetchCreditLimitHistorical stored procedure datas",
                                              handle);
                  }
                break;
              }
            default:
              {
                ERROR_LOG << "Unhandled IDA result type : " << resType << endl;
                break;
              }
            }
        }
    }

  if( returnStatus == 0 )
    {
      KNC_Result res=KNCB_CreditLimit::RELATED_VALIDATION_RESPONSE_CLASS::sendGetHistorisationCurvesSuccess( toSend,
                     handle );
      if(!res)
        {
          throw_LOGICAL(res.text());
        };
    }
  else
    {
      KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM,
                                "FetchCreditLimitHistorical stored procedure call didn't complete properly.",
                                handle);
    }
}

void
KNCB_CreditLimit::onGetByShortNameHistorisationCurves( KNET_Limit::LimitKind limitKind,
    char const *nameCL,
    char const *timebandShortName,
    KGR_Date const & horizonDate,
    KNET_RequestHandle handle )
{
  // todo status
  // StoreProcedure parameters
  char limitKindChar       = *KNETToPSLimitKind(limitKind).c_str();

  char name[40+1];
  char timeband[16+1];


  snprintf(name,16+1,"%s",nameCL);
  snprintf(timeband,16+1,"%s",timebandShortName);

  // bindingParams


  // IDA initialisation
  KT_PtrWrapper< KDBT_DBEnv >             envIDA(new KDBT_DBEnv(serverParams_));
  KT_PtrWrapper< K_CallableStatement_ac > stmt( envIDA->getClbStmt() );

	KGLB_Date kglbDate(horizonDate.getDate().getYear(),
				horizonDate.getDate().getMonth(),
				horizonDate.getDate().getDay());

  stmt->freeStmt();
  stmt->Prepare( "FetchCreditLimitHistoShortName" );
  stmt->BindParam_char  (  1, &limitKindChar );
  stmt->BindParam_string(  2, name, 16+1 );
  stmt->BindParam_string(  3, timeband, 16+1 );
  stmt->BindParam_string(  4, std_const_cast(char *) (kglbDate.toStringDatabaseFormat112().c_str()), 10+1/*horizonDate.getDate().getTimeStr(tmp), 20+1 */);


  // return params
  int returnStatus = 0;
  int execRes      = 0;


  // the KNETData we want to fill
  KGR_Collection<KNET_LimitUseCurves> toSend;

  // handle result
  if( (execRes = stmt->Exec()) != K_DBDef_ac::DB_SUCCESS )
    {
      KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM,
                                "Couldn't execute FetchCreditLimitHistorical store procedure.",
                                handle);
    }
  else
    {
      while( stmt->MoreResult() == K_DBDef_ac::DB_SUCCESS )
        {
          int resType;
          switch( resType = stmt->getResultType() )
            {
            case K_DBDef_ac::STATUS :
              {
                int i = 1;
                stmt->BindCol_int(&i, &returnStatus);
                while( stmt->Fetch() == K_DBDef_ac::DB_SUCCESS )
                {}

                break;
              }
            case K_DBDef_ac::ROWS :
              {
                int bindRes = 0;
                int dummy = 1;

                date_t histoDate;
                double allocated;
                double used;
                double addOn;
                int    dealCount;

                KGR_Collection<double> usedAmounts;
                KGR_Collection<double> availableAmounts;
                KGR_Collection<double> allocationAmounts;
                KGR_Collection<KGR_Date> histoDates;
                KGR_Collection<int>    dealNbr;

                bindRes = stmt->BindCol_date( &dummy, &histoDate );
                if( bindRes == K_DBDef_ac::DB_SUCCESS )
                  bindRes = stmt->BindCol_double( &dummy, &allocated );
                if( bindRes == K_DBDef_ac::DB_SUCCESS )
                  bindRes = stmt->BindCol_double( &dummy, &used );
                if( bindRes == K_DBDef_ac::DB_SUCCESS )
                  bindRes = stmt->BindCol_double( &dummy, &addOn );
                if( bindRes == K_DBDef_ac::DB_SUCCESS )
                  bindRes = stmt->BindCol_int( &dummy, &dealCount );

                if( bindRes == K_DBDef_ac::DB_SUCCESS )
                  {
                    while( stmt->Fetch() == K_DBDef_ac::DB_SUCCESS )
                      {
                        /* be careful, KNC_Date::getTime_t() truncates dates before 1/1/1970 on winnt */
                        KGR_Date histoDateKnc;
                        histoDateKnc.setDate( KNC_Date(histoDate ));
                        histoDates.push_back( histoDateKnc );
                        dealNbr.push_back( dealCount );
                        usedAmounts.push_back( used );
                        availableAmounts.push_back( addOn );
                        allocationAmounts.push_back( allocated );
                      }


                    unsigned long i;
                    for (i=0;i<histoDates.size() ;i++)
                      {
                        KNET_LimitUseCurves curve(i,
                                                  usedAmounts[i],
                                                  availableAmounts[i],
                                                  allocationAmounts[i],
                                                  dealNbr[i],
                                                  histoDates[i]);
                        toSend.push_back( curve );
                      }
                  }
                else
                  {
                    KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM,
                                              "Couldn't fetch FetchCreditLimitHistorical stored procedure datas",
                                              handle);
                  }
                break;
              }
            default:
              {
                ERROR_LOG << "Unhandled IDA result type : " << resType << endl;
                break;
              }
            }
        }
    }

  if( returnStatus == 0 )
    {
      KNC_Result res=KNCB_CreditLimit::RELATED_VALIDATION_RESPONSE_CLASS::sendGetHistorisationCurvesSuccess( toSend,
                     handle );
      if(!res)
        {
          throw_LOGICAL(res.text());
        };
    }
  else
    {
      KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM,
                                "FetchCreditLimitHistorical stored procedure call didn't complete properly.",
                                handle);
    }
}


/*===================================================================================
																				Limit
===================================================================================*/

void
KNCB_CreditLimit::onQueryLimits( KNET_Limit::LimitKind linitKind,
                                 KNET_DoubleValidation::Status *status,
                                 KNET_Limit::RefModeIG const* cptyRefMode,
                                 KGR_Id const* cpty,
                                 KNET_Limit::RefMode const* folderRefMode,
                                 KGR_Id const* folder,
                                 KNET_Limit::RefMode const* countryRefMode,
                                 KGR_Id const* country,
                                 KNET_Limit::RefMode const* industryRefMode,
                                 KGR_Id const* industry,
                                 KNET_Limit::RefMode const* instrumentRefMode,
                                 KGR_Id const* instrument,
                                 KNET_Limit::RefMode const* currencyRefMode,
                                 KGR_Id const* currency,
                                 KNET_Limit::RefMode const* userRefMode,
                                 KGR_Id const* user,
                                 KGR_Id const* limitCoverage,
                                 KGR_Id const* riskWeightCoverage,
                                 KNET_Limit::RefMode const* projectRefMode,
                                 KGR_Id const* projectCoverage,
                                 KGR_Id const* timeBand,
                                 KGR_Id const* ratingAgency,
                                 KGR_Id const* rating,
                                 bool * capitalLimit,
                                 bool * economicCapitalLimit,
                                 KGR_Id const *RequestUser,
                                 KGR_Date const *RequestDateUpperBound,
                                 KGR_Date const *RequestDateLowerBound,
                                 KGR_Id const *ValidationUser,
                                 KGR_Date const *ValidationDateUpperBound,
                                 KGR_Date const *ValidationDateLowerBound,
                                 int maxLenght,
                                 KNET_RequestHandle handle,
                                 KNEL_InMessage inMsg )
{
  kncbtkCreditLimitLimit_.queryLimits( KNETToPSLimitKind(linitKind).c_str(),
                                       status,
                                       cptyRefMode,
                                       cpty,
                                       folderRefMode,
                                       folder,
                                       countryRefMode,
                                       country,
                                       industryRefMode,
                                       industry,
                                       instrumentRefMode,
                                       instrument,
                                       currencyRefMode,
                                       currency,
                                       userRefMode,
                                       user,
                                       limitCoverage,
                                       riskWeightCoverage,
									   projectRefMode,
                                       projectCoverage,
                                       timeBand,
                                       ratingAgency,
                                       rating,
                                       capitalLimit,
                                       economicCapitalLimit,
                                       RequestUser,
                                       RequestDateUpperBound,
                                       RequestDateLowerBound,
                                       ValidationUser,
                                       ValidationDateUpperBound,
                                       ValidationDateLowerBound,
                                       maxLenght,
                                       handle,
                                       &inMsg );
}


void
KNCB_CreditLimit::onQueryLimits( KNET_Limit::LimitKind linitKind,
                                 KNET_DoubleValidation::Status *status,
                                 bool cptyNULL,
                                 KGR_Id const* cpty,
                                 bool folderNULL,
                                 KGR_Id const* folder,
                                 bool countryNULL,
                                 KGR_Id const* country,
                                 bool industryNULL,
                                 KGR_Id const* industry,
                                 bool instrumentNULL,
                                 KGR_Id const* instrument,
                                 bool currencyNULL,
                                 KGR_Id const* currency,
                                 bool userNULL,
                                 KGR_Id const* user,
                                 KGR_Id const* limitCoverage,
                                 bool limitCoverageNULL,
                                 KGR_Id const* riskWeightCoverage,
                                 bool riskWeightCoverageNULL,
								 KGR_Id const* projectCoverage,
                                 bool projectCoverageNULL,
                                 KGR_Id const* timeBand,
                                 bool ratingAgencyNULL,
                                 KGR_Id const* ratingAgency,
                                 bool ratingNULL,
                                 KGR_Id const* rating,
                                 bool * capitalLimit,
                                 bool * economicCapitalLimit,
                                 KGR_Id const *RequestUser,
                                 KGR_Date const *RequestDateUpperBound,
                                 KGR_Date const *RequestDateLowerBound,
                                 KGR_Id const *ValidationUser,
                                 KGR_Date const *ValidationDateUpperBound,
                                 KGR_Date const *ValidationDateLowerBound,
                                 int maxLenght,
                                 KNET_RequestHandle handle,
                                 KNEL_InMessage inMsg)
{

  kncbtkCreditLimitLimit_.queryLimits(KNETToPSLimitKind(linitKind).c_str(),
                                      status,
                                      cptyNULL,
                                      cpty,
                                      folderNULL,
                                      folder,
                                      countryNULL,
                                      country,
                                      industryNULL,
                                      industry,
                                      instrumentNULL,
                                      instrument,
                                      currencyNULL,
                                      currency,
                                      userNULL,
                                      user,
                                      limitCoverage,
                                      limitCoverageNULL,
                                      riskWeightCoverage,
                                      riskWeightCoverageNULL,
                                      projectCoverage,
                                      projectCoverageNULL,
                                      timeBand,
                                      ratingAgencyNULL,
                                      ratingAgency,
                                      ratingNULL,
                                      rating,
                                      capitalLimit,
                                      economicCapitalLimit,
                                      RequestUser,
                                      RequestDateUpperBound,
                                      RequestDateLowerBound,
                                      ValidationUser,
                                      ValidationDateUpperBound,
                                      ValidationDateLowerBound,
                                      maxLenght,
                                      handle,
                                      &inMsg);
}


void KNCB_CreditLimit::onMicroBatchQuery( int                       maxLength,
    KGR_Id const             *cptyId,
    KGR_Id const             *folderId,
    KGR_Id const             *countryId,
    KGR_Id const             *industryId,
    KGR_Id const             *currencyId,
    KGR_Id const             *knuserId,
    KGR_Id const             *ratingAgencyId,
    KGR_Id const             *ratingId,
    KGR_Id const             *rwAssetOrProductExposureId,
    KGR_Id const             *projectCoverageId,
    bool                      capitalLimit,
    bool                      economicCapitalLimit ,
    KNET_RequestHandle const &handle )
{
  //
  // A NOTER : "rwAssetOrProductExposure", si non null, represente soit un
  //           un risk weight asset, soit un product exposure en fonction
  //           du parametre "capitalLimit"
  //

  static const char *fctName = "KNCB_CreditLimit::onMicroBatchQuery";
 INFO_LOG << "Querying Credit Limits " << std::endl ;

  KGLDB_WhereClause whereClause;

  if ( capitalLimit )
    whereClause.addCondition("CapitalLimit", "=", true);
  else
    whereClause.addCondition("CapitalLimit", "=", false);

  if ( economicCapitalLimit )
    whereClause.addCondition("EconomicCapitalLimit", "=", true);
  else
    whereClause.addCondition("EconomicCapitalLimit", "=", false);

  if ( cptyId )
    {
      string cptyIdStr = KNC_ConvId::idToStr( cptyId->getValue() );
      string cptyCoverageStr = " AND ((CptyId_Coverage = 0x" + cptyIdStr + ") OR (CptyId_Coverage IN (SELECT CptyIdParent FROM LinkedCpty WHERE CptyIdChild = 0x" + cptyIdStr + ")))";
      whereClause.addExpression( cptyCoverageStr.c_str() );
    }

  if ( folderId )
    {
      string 	folderIdStr = KNC_ConvId::idToStr( folderId->getValue() );
      string folderCoverageStr = " AND ((FolderId_Coverage = 0x" + folderIdStr + ") OR (FolderId_Coverage IN (SELECT FolderIdParent FROM LinkedFolder WHERE FolderIdChild = 0x" + folderIdStr + ")))";
      whereClause.addExpression( folderCoverageStr.c_str() );
    }

  if ( countryId )
    {
      string 	countryIdStr = KNC_ConvId::idToStr( countryId->getValue() );
      string countryCoverageStr = " AND ((CountryId_Coverage = 0x" + countryIdStr + ") OR (CountryId_Coverage IN (SELECT CountryIdParent FROM LinkedCountry WHERE CountryIdChild = 0x" + countryIdStr + ")))";
      whereClause.addExpression( countryCoverageStr.c_str() );
    }

  if ( industryId )
    {
      string 	industryIdStr = KNC_ConvId::idToStr( industryId->getValue() );
      string industryCoverageStr = " AND ((IndustryId_Coverage = 0x" + industryIdStr + ") OR (IndustryId_Coverage IN (SELECT IndustryIdParent FROM LinkedIndustry WHERE IndustryIdChild = 0x" + industryIdStr + ")))";
      whereClause.addExpression( industryCoverageStr.c_str() );
    }

  if ( currencyId )
    {
      string 	currencyIdStr = KNC_ConvId::idToStr( currencyId->getValue() );
      string currencyCoverageStr = " AND ((CurrencyId_Coverage = 0x" + currencyIdStr + ") OR (CurrencyId_Coverage IN (SELECT CurrencyIdParent FROM LinkedCurrency WHERE CurrencyIdChild = 0x" + currencyIdStr + ")))";
      whereClause.addExpression( currencyCoverageStr.c_str() );
    }

  if ( knuserId )
    {
      string 	knuserIdStr = KNC_ConvId::idToStr( knuserId->getValue() );
      string knuserCoverageStr = " AND ((KNUserId_Coverage = 0x" + knuserIdStr + ") OR (KNUserId_Coverage IN (SELECT KNUserIdParent FROM LinkedKNUser WHERE KNUserIdChild = 0x" + knuserIdStr + ")))";
      whereClause.addExpression( knuserCoverageStr.c_str() );
    }

  if ( ratingAgencyId )
    {
      string 	ratingAgencyIdStr = KNC_ConvId::idToStr( ratingAgencyId->getValue() );
      string ratingAgencyCoverageStr = " AND (RatingAgencyId = 0x" + ratingAgencyIdStr + ")";
      whereClause.addExpression( ratingAgencyCoverageStr.c_str() );
    }

  if ( ratingId )
    {
      string 	ratingIdStr = KNC_ConvId::idToStr( ratingId->getValue() );
      string ratingCoverageStr = " AND (RatingId_Coverage = 0x" + ratingIdStr + ")";
      whereClause.addExpression( ratingCoverageStr.c_str() );
    }

  if ( rwAssetOrProductExposureId )
    {
      if ( capitalLimit )
        {
          string riskWeightCoverageIdStr = KNC_ConvId::idToStr( rwAssetOrProductExposureId->getValue() );
          string riskWeightCoverageStr = " AND (RiskWeightCoverageId = 0x" + riskWeightCoverageIdStr + ")";
          whereClause.addExpression( riskWeightCoverageStr.c_str() );
        }
      else
        {
          string productExposureIdStr = KNC_ConvId::idToStr( rwAssetOrProductExposureId->getValue() );
          string productExposureStr = " AND (CreditLimitCoverageId = 0x" + productExposureIdStr + ")";
          whereClause.addExpression( productExposureStr.c_str() );
        }
    }

	if ( projectCoverageId )
    {
      string projectCoverageIdStr = KNC_ConvId::idToStr( projectCoverageId->getValue() );
      string projectCoverageStr = " AND (KGRProjectId_Coverage = 0x" + projectCoverageIdStr + ")";
      whereClause.addExpression( projectCoverageStr.c_str() );
    }

	string limitKindStr = " AND ((LimitKind = 'C') OR (LimitKind = 'S'))"; 	
	whereClause.addExpression( limitKindStr.c_str());


  CreditLimitMaster_Cltn_var creditLimitMasterColl;

  creditLimitMasterColl = CreditLimitMaster_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());
  if( !PS_is_nil(creditLimitMasterColl) && creditLimitMasterColl->length() )
    {
      KGR_Collection< KNET_CreditLimitAccess > creditLimitAccessCollection;

      unsigned long creditLimitMasterCollSize = 0;
      creditLimitMasterCollSize = creditLimitMasterColl->length();

      unsigned long i=0;
	for ( i=0; i < creditLimitMasterCollSize && i < (unsigned long) maxLength ; i++ )
        {
          CreditLimitMaster_var const &creditLimitMaster = creditLimitMasterColl[i];


          if(PS_is_nil(creditLimitMaster))
            continue;

          KNET_CreditLimitAccess 	knetCreditLimitAccess;

          PSToKNET(creditLimitMaster, knetCreditLimitAccess);
          creditLimitAccessCollection.push_back( knetCreditLimitAccess );
        }

      int resultCount = 0;
      resultCount = creditLimitAccessCollection.size();

      //if ( resultCount > maxLength)
      //   resultCount = maxLength;

      KGL_DataCollResponse<KNET_CreditLimitAccess>::sendSuccess( creditLimitAccessCollection,
          resultCount,
          handle );
    }
  else
    {
      KGL_Response::sendFailure( KNC_FailureCategory::NOTFOUND, "No Credit Limits retreived !" , handle );
    }
}

void KNCB_CreditLimit::onQueryLimitsByStatus(KGR_Id & UserWhoCalled,
    								   		 KNET_LimitStatus::LimitState limitStatus,
	    								     KNET_Limit::LimitKind limitKind,
	 									     KNET_DoubleValidation::Status *status,
										     KNET_Limit::RefModeIG const* cptyRefMode,
										     KGR_Id const* cpty,
										     KNET_Limit::RefMode const* folderRefMode,
										     KGR_Id const* folder,
										     KNET_Limit::RefMode const* countryRefMode,
										     KGR_Id const* country,
										     KNET_Limit::RefMode const* industryRefMode,
										     KGR_Id const* industry,
										     KNET_Limit::RefMode const* instrumentRefMode,
										     KGR_Id const* instrument,
										     KNET_Limit::RefMode const* currencyRefMode,
										     KGR_Id const* currency,
										     KNET_Limit::RefMode const* userRefMode,
										     KGR_Id const* user,
										     KGR_Id const* limitCoverage,
										     KGR_Id const* riskWeightCoverage,
											 KNET_Limit::RefMode const* projectRefMode,
										     KGR_Id const* projectCoverage,
										     KGR_Id const* timeBand,
										     KGR_Id const* ratingAgency,
										     KGR_Id const* rating,
										     bool * capitalLimit,
										     bool * economicCapitalLimit,
										     KGR_Id const *RequestUser,
										     KGR_Date const *RequestDateUpperBound,
										     KGR_Date const *RequestDateLowerBound,
										     KGR_Id const *ValidationUser,
										     KGR_Date const *ValidationDateUpperBound,
										     KGR_Date const *ValidationDateLowerBound,
										     int maxLenght,
										     KNET_RequestHandle handle,
										     KNEL_InMessage inMsg)
{
	bool  KGL_NO_DASHBOARD = (serverParams_.dashboardEnabled_ == false);
	static const char * KGL_NO_DASHBOARD_CREDIT_LIMIT = getenv("KGL_NO_DASHBOARD_CREDIT_LIMIT");
	if (KGL_NO_DASHBOARD ||
		KGL_NO_DASHBOARD_CREDIT_LIMIT)
	{
		WARNING_LOG << "KNCB_CreditLimit::onQueryLimitsByStatus : BLOCKED by dashboardEnabled_ = false or KGL_NO_DASHBOARD_CREDIT_LIMIT variable !!!" << endl;
		return ;
	}

	KNC_Result	res;
	KDBT_DBConnectionUser*	pDBConnection = KNSDBC_DBConnection::instance().getKglDbConnection();
	KNCB_CreditLimitDashboardsDataFetcher	Fetcher(pDBConnection);
	int									 	nNbrDays;
	KNC_Date								Today, DummyDate;
	KNCB_Calendar *							pInstance = KNCB_Calendar::instance();

	KNEL_OpaqueValue opaqueValue;
	res = inMsg.getFieldValue ("asyncReplyInbox", opaqueValue);
	if (!res)
		return;
    string responseInbox = (char*) opaqueValue.getData();

	// Find user config to extract Currency of Dashboard and Number Of days for historic research
	KNUserConfig_var UserConfig = KNCBTK_CoreBasic<KNUserConfig_var,KNUserConfig_Factory>
									::queryId(UserWhoCalled);

	if (PS_is_nil(UserConfig))
		return ;

	Today.Now();
	KGR_Id CurrencyId((*UserConfig).DashboardCurrencyId()->getOidVal());
	pInstance->previousBusinessDay(CurrencyId,
								   Today,
								   DummyDate,
								   nNbrDays,
								   (*UserConfig).DashboardHistoryDays());

	// Execute SP and return a list of results matching the parameters
	res = Fetcher.exec(UserWhoCalled,
					   limitStatus,
					   limitKind,
			           status,
			           cptyRefMode,
			           cpty,
			           folderRefMode,
			           folder,
			           countryRefMode,
			           country,
			           industryRefMode,
			           industry,
			           instrumentRefMode,
			           instrument,
			           currencyRefMode,
			           currency,
			           userRefMode,
			           user,
			           limitCoverage,
			           riskWeightCoverage,
					   projectRefMode,
			           projectCoverage,
			           timeBand,
			           ratingAgency,
			           rating,
			           capitalLimit,
			           economicCapitalLimit,
			           RequestUser,
			           RequestDateUpperBound,
			           RequestDateLowerBound,
			           ValidationUser,
			           ValidationDateUpperBound,
			           ValidationDateLowerBound,
			           maxLenght,
			           nNbrDays);

	if (!res)
	{
		ERROR_LOG << "KNCB_CreditLimit::onQueryLimitsByStatus: Stored Procedure Error" << endl;
		return ;
	}

	const vector<KNET_CreditLimitAccess> & MsgOut = Fetcher.GetLoadedObject();

	KGL_CreditLimitAdapterVectorImpl	ResponseListObject;

	ResponseListObject.setRawData(MsgOut);
	ResponseListObject.setObjectType(KGLE_AsyncFwkObjectType::CREDITLIMIT);

	if (limitStatus == KNET_LimitStatus::KNET_EXCESS)
		KGLAF_AsyncFwk::instance().sendNotification(KGLE_AsyncMsgType::LIMIT_BREACHED,
																ResponseListObject,
																&responseInbox);
	else if (limitStatus == KNET_LimitStatus::KNET_NEARLY_EXCEEDED)
		KGLAF_AsyncFwk::instance().sendNotification(KGLE_AsyncMsgType::LIMIT_NR_EXCEEDED,
																ResponseListObject,
																&responseInbox);
	else if (limitStatus == KNET_LimitStatus::KNET_NEARLY_EXPIRING)
		KGLAF_AsyncFwk::instance().sendNotification(KGLE_AsyncMsgType::LIMIT_NR_EXPIRING,
																ResponseListObject,
																&responseInbox);
	else if (limitStatus == KNET_LimitStatus::KNET_RECENTLY_CREATED)
		KGLAF_AsyncFwk::instance().sendNotification(KGLE_AsyncMsgType::INSERTED,
																ResponseListObject,
																&responseInbox);
}

/*===================================================================================
  NamedData (PARTIAL : no getByName/ShortName)
  ===================================================================================*/


void KNCB_CreditLimit::onAccept( KGR_Id const      &id,
                                 KNET_RequestHandle  handle )
{
  accept( id, handle );
}


void KNCB_CreditLimit::onReject( KGR_Id const      &id,
                                 KNET_RequestHandle  handle )
{
  reject( id, handle );
}


void KNCB_CreditLimit::onInsert( KGR_DataChange const &data,
                                 KNET_RequestHandle     handle )
{
	actualMode_=INSERT_MODE;
  RELATED_KNET_CLASS_CHANGE const &casted =
    dynamic_cast<RELATED_KNET_CLASS_CHANGE const&>(data);

  validationOrStdInsert( casted, handle );
}


void KNCB_CreditLimit::onUpdate( KGR_Id const         &id,
                                 KGR_DataChange const &data,
                                 KNET_RequestHandle     handle )
{
actualMode_=UPDATE_MODE;
  KNDB_LOOP_BEGIN
  try
    {
      KNDB_T_READ

      CreditLimitMaster_var clMaster = getVar<CreditLimitMaster>( id );

      if( PS_is_nil( clMaster ) )
        {
          KNDB_T_ROLLBACK
          string errMsg( CreditLimitMaster_Factory::instance()->className() );
          errMsg += "Not Found ";
          KGL_Response::sendFailure( KNC_FailureCategory::NOTFOUND,
                                     errMsg.c_str(), handle );
          return;
        }

      if( !CreditLimitMaster_Factory::instance()->hasAccess( false, true, clMaster,
          toPS( handle->getUser() ) ) )
        throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
      if(!PS_is_nil(clMaster->arcCptyCoverage()) &&
          !Cpty_Factory::instance()->hasAccess(2,false, true,clMaster->arcCptyCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }
      if(!PS_is_nil(clMaster->arcFolderCoverage()) &&
          !Folder_Factory::instance()->hasAccess(2,false, true,clMaster->arcFolderCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }

      KNDB_T_COMMIT
    }
  catch (const PS_ServerError& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
          KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
          return;
        }
    }
  KNDB_LOOP_END


  RELATED_KNET_CLASS_CHANGE const &casted =
    dynamic_cast<RELATED_KNET_CLASS_CHANGE const&>(data);

  validationOrStdUpdate( id, casted, handle );
}


void KNCB_CreditLimit::onRemove( KGR_Id const      &id,
                                 KNET_RequestHandle  handle )
{
	actualMode_=REMOVE_MODE;
  //
  KNDB_LOOP_BEGIN
  try
    {
      KNDB_T_READ

      KNUser_var psUser = KNCBTK_CoreBasic<KNUser_var
                          ,KNUser_Factory>
                          ::queryId(handle->getUser());
      if (PS_is_nil(psUser))
        {
          KNDB_T_ROLLBACK
          string errMsg(KNUser_Factory::instance()->className());
          errMsg+="Not Found ";
          KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
          return;
        }


      CreditLimitMaster_var psCreditLimit = KNCBTK_CoreBasic<CreditLimitMaster_var
                                            ,CreditLimitMaster_Factory>
                                            ::queryId(id);
      if (PS_is_nil(psCreditLimit))
        {
          KNDB_T_ROLLBACK
          string errMsg(CreditLimitMaster_Factory::instance()->className());
          errMsg+="Not Found ";
          KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
          return;
        }
      if(!CreditLimitMaster_Factory::instance()->hasAccess(false,true,psCreditLimit,psUser->Id()))
        {
          throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }
      if(!PS_is_nil(psCreditLimit->arcCptyCoverage()) &&
          !Cpty_Factory::instance()->hasAccess(2,false, true,psCreditLimit->arcCptyCoverage(),psUser->Id()))
        {
          throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }
      if(!PS_is_nil(psCreditLimit->arcFolderCoverage()) &&
          !Folder_Factory::instance()->hasAccess(2,false, true,psCreditLimit->arcFolderCoverage(),psUser->Id()))
        {
          throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }
	
	// test if the Limit is the source of an allocation transfer.
	CreditLimit_Cltn_var clCltn = psCreditLimit->arcCreditLimits();

	if(!PS_is_nil( clCltn))
	{
		for(unsigned long idx=0;idx < clCltn->length();++idx)
		{
			CreditLimit_var cl = clCltn[idx];
			char whereClause[255];
			sprintf(whereClause,
					" CreditLimitId_Transfer=0x%s AND AllocatedAmount < 0 ", 
					KNC_ConvId::idToStr( (const char*) cl->Id()->getOidVal() ).c_str());

			CreditReservation_Cltn_var crCltn = CreditReservation_Factory::instance()->querySQLWhere(whereClause);
			if(!PS_is_nil(crCltn)&& crCltn->length())
				throw_LOGICAL(LIMIT_IS_SOURCE_OF_ALLOCATION_TRANSFER);
		}
	}

      KNDB_T_COMMIT
      //
    }
  catch (const PS_ServerError& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
          KGL_Response::sendFailure(KNC_FailureCategory::SYSTEM, e.description, handle);
          return;
        }
    }
  KNDB_LOOP_END

  validationOrStdDelete( id, handle );
}


void KNCB_CreditLimit::basicDelete( KNCB_CreditLimit::RELATED_PS_COV_CLASS_VAR doomed )
{
  KNCB_AutoAggregMutex mutex(serverParams_);

  KNDB_BeginReadWriteSection();
  RELATED_PS_COV_FACTORY::instance()->remove
  ( doomed );
  KNDB_EndReadWriteSection();
}


void KNCB_CreditLimit::onGetByIdentifier( KGR_Id const      &id,
    KNET_RequestHandle  handle )
{
  //	kncbtkCreditLimitNamedData_.getByIdentifier(id, handle);

  getLimitByIdentifierIfAccessAllowed< RELATED_PS_COV_CLASS_VAR,
  RELATED_KNET_CLASS_ACCESS,
  RELATED_VALIDATION_RESPONSE_CLASS >( this, id, handle );

}


void KNCB_CreditLimit::onGetDelta(KGR_Id const      &id,
                                  KNET_RequestHandle  handle )
{
  getDelta( id, handle );
}


/*===================================================================================
																				Access
===================================================================================*/


void KNCB_CreditLimit::onInsertAccess( KGR_Identifier const   &dataId,
                                       KNET_AccessChange const &access,
                                       KNET_RequestHandle       handle )
{
  kncbtkCreditLimitAccess_.insertAccess( (KGR_Id const &)dataId,
                                         access,
                                         handle );
}


void KNCB_CreditLimit::onUpdateAccess( KGR_Identifier const   &dataId,
                                       KGR_Id const           &accessId,
                                       KNET_AccessChange const &access,
                                       KNET_RequestHandle       handle )
{
  kncbtkCreditLimitAccess_.updateAccess( (KGR_Id const &)dataId,
                                         accessId,
                                         access,
                                         handle );
}


void KNCB_CreditLimit::onRemoveAccess( KGR_Identifier const &dataId,
                                       KGR_Id const         &accessId,
                                       KNET_RequestHandle     handle )
{
  kncbtkCreditLimitAccess_.removeAccess( (KGR_Id const &)dataId,
                                         accessId,
                                         handle );
}


void KNCB_CreditLimit::onQueryAccess( KGR_Identifier const &dataId,
                                      KNET_RequestHandle     handle )
{
  kncbtkCreditLimitAccess_.queryAccess( (KGR_Id const &) dataId, handle );
}


///////////////////
// inherited tools
/////////////////


/* FORCE INSTANCIATION */
template class KNCBTK_ValidableData< KNCB_CreditLimit,
KNET_CreditLimitChange,
KNET_CreditLimitAccess,
CreditLimitMaster_Factory,
CreditLimitMaster_var,
KNET_CreditLimitResponse,
CLMasterToCheck_var,
CLMasterToCheck_Factory,
CLMasterDVInsert_var,
CLMasterDVCoverage_var,
CLMasterDVCoverage_Factory,
CreditLimitMasterBase_var,
KGL_CreditLimitAdapterVectorImpl,
KGL_CreditLimitAdapterImpl,
KGLE_AsyncMsgType::DV_LIMIT>
;



void KNCB_CreditLimit::simpleKNETToBasePS( KNET_RequestHandle               hdl,
    RELATED_KNET_CLASS_CHANGE const &knetData,
    RELATED_PS_BASE_CLASS_VAR        core,
    bool                             setMandatoryFields )
{
  if( setMandatoryFields )
    {
      core->arcCurrency    ( getVar<Currency>( *knetData.getCurrency(), hdl->getSource() ) );
      core->AllocatedAmount( knetData.getAllocatedAmount() );
      core->AllocationDate ( time_tToPS(knetData.getAllocationDate()).c_str() );
      core->Locked         ( knetData.getLocked() );
      core->BatchOnly      ( knetData.getImpactBatchOnly() );
      core->FullMaturity   ( knetData.getFullMaturity() );
      core->CreditMethod   ( KNETToPSCreditMethod(knetData.getCreditMethod()).c_str() );
      core->UseTimeBand    ( knetData.getUseTimeBand() );
      core->HasSchedule    ( knetData.getHasSchedule() );
      core->AutomaticAllocationTransfert( knetData.getAutomaticAllocTransfer() );
      core->UseVDV         ( knetData.getUseValueDateReview() );
      core->IsEntity       ( knetData.getIsEntity() );
      core->LimitGroup     ( knetData.getLimitGroup() );
   }

  // null allowed in the database but it's conceptually mandatory
  // force knetData update even if it's const to synchronise name
  // and shortName between DB and this data.
  setNameAndShortName( *core, knetData );

  if( knetData.isBeginDateNULL() )
    core->BeginDateNULL( true );
  else
    core->BeginDate( KNET_DateToPS(knetData.getBeginDate()).c_str() );

  if( knetData.isEndDateNULL() )
    core->EndDateNULL( true );
  else
    core->EndDate( KNET_DateToPS(knetData.getEndDate()).c_str() );

  if( knetData.isLockDateNULL() )
    core->LockDateNULL( true );
  else
    core->LockDate( KNET_DateToPS(knetData.getLockDate()).c_str() );

  if( knetData.isEnforcedNULL() )
    core->EnforcedNULL( true );
  else
    core->Enforced( knetData.getEnforced() );

  if( knetData.isAnnotationNULL() )
    core->AnnotationNULL( true );
  else
    core->Annotation( knetData.getAnnotation() );

  //Fix for 00012487.KRE : Limit double validation does not work for limit reviewer
  KGR_Id const &src = hdl->getSource();
  typedef RELATED_KNET_CLASS_CHANGE TP;
  typedef KNET_LimitChange          BT;
  BT const &base = knetData;

  core->arcReviewer( getVarOrNull<KNUser>( base, &BT::isLimitReviewerNULL,
                     &BT::getLimitReviewer, src ) );

  if( knetData.isMessageNULL() ||  string(knetData.getMessage()).length() == 0)
    core->MsgNULL( true );
  else{
	  core->Msg( knetData.getMessage() );
  }

  if( knetData.isMessageOnLockNULL() ||  string(knetData.getMessageOnLock()).length() == 0 )
    core->MessageOnLockNULL( true );
  else
    core->MessageOnLock( knetData.getMessageOnLock() );

  if( knetData.isAmountTypeNULL() )
      core->AmountTypeNULL( true );
  else {
	string c_amountType = "S";
	c_amountType = KNDBC_ConvChoice::KNET2Ps_AmountType(knetData.getAmountType());
	core->AmountType(c_amountType.c_str());
	}

}


void KNCB_CreditLimit::KNETToCovPS( KNET_RequestHandle               hdl,
                                    RELATED_KNET_CLASS_CHANGE const &knetData,
                                    RELATED_PS_COV_CLASS_VAR         core,
                                    bool                             setMandatoryFields )
{
  // no more overdraft mode nor used amount, both are linked to CreditLimit
  KGR_Id src( hdl->getSource() );

  simpleKNETToBasePS( hdl, knetData,
                      std_static_cast( RELATED_PS_BASE_CLASS_VAR )( core ),
                      setMandatoryFields );

  KGR_Collection<KGL_TimeBandCoverageElementChange> const &TBCoverageColl =
    knetData.getTimeBandCoverageElement();

  if(TBCoverageColl.size()<1)
    {
		if( !knetData.isLimitCoverageNULL() )
		{
			//If we have a defaut Timeband in the Product Exposure we need to use it instead of 0d-+
			CreditLimitCoverage_var  limCovv=getVar<CreditLimitCoverage>( knetData.getLimitCoverage() );

			if (!limCovv->TimeBandIdNULL() && actualMode_==INSERT_MODE)
				{
					TimeBand_var psTimeBand = TimeBand_Factory::instance()->queryKey( *limCovv->TimeBandId(), PS_Defs::k_cacheThenDatabase );

					TimeBandCoverageElt_var timeBandCoverageElement= TimeBandCoverageElt_Factory::instance()
					->create( knetData.getAllocatedAmount(),false,core,
							  psTimeBand );
				}
			else
			{
		      // 0D-+ : a default value supposed to be allways available in the database
		      TimeBand_var
		      psTimeBand            = TimeBand_Factory::instance()->queryShortName( INFINIT_TB_SHORTNAME );
		      core->arcTimeBand(psTimeBand);
			}
		}
		else
		{

	      // 0D-+ : a default value supposed to be allways available in the database
	      TimeBand_var
	      psTimeBand            = TimeBand_Factory::instance()->queryShortName( INFINIT_TB_SHORTNAME );

	      core->arcTimeBand(psTimeBand);
		}
    }
  else
    {
      core->arcTimeBand(TimeBand_var());
    }

  // Mandatory attributes
  if( setMandatoryFields )
    {
      //  		core->arcCreditLimitCoverage( getVar<CreditLimitCoverage>(knetData.getLimitCoverage()) );
      core->RefMode_Cpty(KNETToPSRefModeIG(knetData.getCptyRefMode()).c_str());
      core->RefMode_Industry(KNETToPSRefMode(knetData.getIndustryRefMode()).c_str());
      core->RefMode_Instrument(KNETToPSRefMode(knetData.getInstrumentRefMode()).c_str());
      core->RefMode_Country(KNETToPSRefMode(knetData.getCountryRefMode()).c_str());
      core->RefMode_Folder(KNETToPSRefMode(knetData.getFolderRefMode()).c_str());
      core->RefMode_Currency(KNETToPSRefMode(knetData.getCurrencyRefMode()).c_str());
      core->RefMode_KNUser(KNETToPSRefMode(knetData.getUserRefMode()).c_str());
	  core->RefMode_KGRProject(KNETToPSRefMode(knetData.getProjectRefMode()).c_str());
      core->LimitKind(KNETToPSLimitKind(knetData.getLimitKind()).c_str());
      core->SovereignKind(KNETToPSSovereignKind(knetData.getSovereignKind()).c_str());
      core->CapitalLimit(knetData.getCapitalLimit());
      core->EconomicCapitalLimit(knetData.getEconomicCapitalLimit());
    }

  typedef RELATED_KNET_CLASS_CHANGE TP;
  typedef KNET_LimitChange          BT;
  BT const &base = knetData;


  // NULL allowed attributes

  // CreditLimitCoverage is supposed to be null if RiskWeightCoverage is not null
  if( !knetData.isLimitCoverageNULL() )
    {
      core->arcCreditLimitCoverage( getVar<CreditLimitCoverage>( knetData.getLimitCoverage() ) );
      core->arcRiskWeightCoverage(RiskWeightCoverage_var());
    }
  else
    {
      core->arcCreditLimitCoverage( CreditLimitCoverage_var() );
    }

  core->arcRiskWeightCoverage( getVarOrNull<RiskWeightCoverage>( knetData, &TP::isRiskWeightCoverageNULL,
                               &TP::getRiskWeightCoverage ) );
  core->arcCptyCoverage( getVarOrNull<Cpty>( base, &BT::isCptyCoverageNULL,
                         &BT::getCptyCoverage, src ) );
  core->arcIndustryCoverage( getVarOrNull<Industry>( base, &BT::isIndustryCoverageNULL,
                             &BT::getIndustryCoverage, src ) );
  core->arcInstrumentCoverage( getVarOrNull<Instrument>( base, &BT::isInstrumentCoverageNULL,
                               &BT::getInstrumentCoverage, src ) );
  core->arcCountryCoverage( getVarOrNull<Country>( base, &BT::isCountryCoverageNULL,
                            &BT::getCountryCoverage, src ) );
  core->arcFolderCoverage( getVarOrNull<Folder>( base, &BT::isFolderCoverageNULL,
                           &BT::getFolderCoverage, src ) );
  core->arcRatingCoverage( getVarOrNull<Rating>( base, &BT::isRatingCoverageNULL,
                           &BT::getRatingCoverage, src ) );
  core->arcRatingAgency( getVarOrNull<RatingAgency>( base, &BT::isRatingAgencyCoverageNULL,
                         &BT::getRatingAgencyCoverage, src ) );
  core->arcCurrencyCoverage( getVarOrNull<Currency>( base, &BT::isCurrencyCoverageNULL,
                             &BT::getCurrencyCoverage, src ) );
  core->arcKGRProjectCoverage( getVarOrNull<KGRProject>(  knetData , &TP::isProjectCoverageNULL,
                             &TP::getProjectCoverage ) );

  if( knetData.isUserCoverageNULL() )
    core->arcKNUserCoverage( KNUser_var() );
  else
    {
      KNUser_var psUser = getVar<KNUser>( *knetData.getUserCoverage(), src );

      TODO( "Change this char enum value into a real enumarated one" );
      if( psUser->Purpose().buff()[0] == 'A' )
        throw_LOGICAL( "User Coverage should have User Identification as Purpose" );

      core->arcKNUserCoverage( psUser );
    }

  if ( ! knetData.isAmountTypeNULL())
  {
		string c_amountType = "S";
		c_amountType = KNDBC_ConvChoice::KNET2Ps_AmountType(knetData.getAmountType());
		core->AmountType(c_amountType.c_str());
  }

}


void KNCB_CreditLimit::KNETToBasePS( KNET_RequestHandle               hdl,
                                     RELATED_KNET_CLASS_CHANGE const &data,
                                     RELATED_PS_BASE_CLASS_VAR        object )
{

	KH_DBG::dbg("KNCB_CreditLimit::KNETToBasePS::method_start");
  simpleKNETToBasePS( hdl, data, object );

  // don't forget to create sub objects
  updateAllocationSchedule( object, data, hdl );

  // As current function is used for DV, we must not call updateTBCoverageElt
  // function else it would create CreditLimits and thus impact computations.
  removeTBCoverageElt( object, hdl );
  insertTBCoverageElt( object, data, hdl );

  // we cannot call update directly else it would try to update last and next
  // review date. We don't want of this behavior
  removeReviewDate( object, hdl );
  insertReviewDate( object, data, hdl );

  // we don't want to create Credit Limits during a CreditLimitMaster DV update
  //	insertCreditLimitElements( object, castedData, handle );

  // last and next review dates don't exist on the toCheck level => no update
  //	updateLastAndNextReviewDateFields( object, data, hdl );

  KH_DBG::dbg("KNCB_CreditLimit::KNETToBasePS::method_end");

}


void KNCB_CreditLimit::DeltaPSToKNET( RELATED_PS_DELTA_CLASS_VAR const  baseDeltaVar,
                                      RELATED_KNET_CLASS_ACCESS        &knetDataAccess )
{
  PSBaseToKNET( *baseDeltaVar, knetDataAccess );
}


KNCB_CreditLimit::RELATED_PS_DELTA_CLASS_VAR
KNCB_CreditLimit::createDeltaFromKNET( KNET_RequestHandle               hdl,
                                       RELATED_PS_CLASS_VAR             base,
                                       RELATED_KNET_CLASS_CHANGE const &data )
{
	KH_DBG::dbg("KNCB_CreditLimit::createDeltaFromKNET::method_start");
	string       allocationDate = time_tToPS( data.getAllocationDate() );
	string       creditMethode  = KNETToPSCreditMethod( data.getCreditMethod() );
	PS_Oid_var   relatedId      = base->Id();
	Currency_var psCurrency     = getVar<Currency>( *data.getCurrency(),
													hdl->getSource() );
	RELATED_PS_DELTA_CLASS_VAR object =
		RELATED_PS_DELTA_FACTORY::instance()->create( data.getAllocatedAmount(),
													  allocationDate.c_str(),
													  data.getFullMaturity(),
													  creditMethode.c_str(),
													  data.getLocked(),
													  data.getImpactBatchOnly(),
													  data.getUseTimeBand(),
													  data.getHasSchedule(),
													  data.getAutomaticAllocTransfer(),
													  data.getUseValueDateReview(),
													  data.getEconomicCapitalLimit(),
													  data.getLimitGroup(),
													  data.getIsEntity(),
													  base,
													  psCurrency );

	if( PS_is_nil( object ) )
		return object;

	simpleKNETToBasePS( hdl, data,
						std_static_cast(CreditLimitMasterBase_var)( object ),
						false );

	// don't forget to create sub objects
	insertReviewDate( object, data, hdl );
	insertAllocationSchedule( object, data, hdl );
	insertTBCoverageElt( object, data, hdl );

	// we don't want to create Credit Limits during a CreditLimitMaster DV update
	//	insertCreditLimitElements( object, castedData, handle );

	// last and next review dates don't exist on the toCheck level => no update
	// updateLastAndNextReviewDateFields( object, data, hdl );
	KH_DBG::dbg("KNCB_CreditLimit::createDeltaFromKNET::method_end");
	return object;
}


void KNCB_CreditLimit::dumpDelta( KNET_RequestHandle         handle,
                                  RELATED_PS_DELTA_CLASS_VAR delta,
                                  RELATED_PS_CLASS_VAR       base )
{

	KH_DBG::dbg("KNCB_CreditLimit::dumpDelta::method_start");
  RELATED_KNET_CLASS_ACCESS access;

  // store in an access data all current fields
  PSToKNET( base, access );

  // override updatable ones with what is available in delta part.
  PSBaseToKNET( * std_static_cast( CreditLimitMasterBase_var )( delta ), access );

  // create a change data from it
  RELATED_KNET_CLASS_CHANGE change( access );

  // call KNETToPS to update current record
  KNETToPS( handle, change, base, true );

  // finally update its sub fields.
  updateReviewDate( base, change, handle );

  updateTBCoverageElt( base, change, handle );

  updateCreditLimitElements( base, change, handle);

  updateAllocationSchedule( base, change, handle );
  KH_DBG::dbg("KNCB_CreditLimit::dumpDelta::method_end");
}


void KNCB_CreditLimit::stdInsert( RELATED_KNET_CLASS_CHANGE const &data,
                                  KNET_RequestHandle handle )
{
  kncbtkCreditLimitNamedData_.insert(data, handle);
}



void KNCB_CreditLimit::stdUpdate( KGR_Id const& id,
                                  RELATED_KNET_CLASS_CHANGE const& data,
                                  KNET_RequestHandle handle )
{
  kncbtkCreditLimitNamedData_.update(id, data, handle);
}


void KNCB_CreditLimit::stdDelete( KGR_Id const& id,
                                  KNET_RequestHandle handle )
{
  //
  KNDB_Mutex aggrMutex(KNDB_Mutex::KNET_MUTEX_AGGREGATION);
  while (!aggrMutex.EnterCS_Trans()) { sleep(1); }
  kncbtkCreditLimitNamedData_.remove(id, handle);
  while (!aggrMutex.LeaveCS_Trans()) { sleep(1); }
}


/*
*================================ TOOL ================================
*/
/*
* PSToKNETNoRisk
*/
KGR_MultiChoice<KNET_CreditDeal::RiskChoice>
KNCB_CreditLimit::PSToKNETNoRisk(long psNoRisk)
{
  KGR_MultiChoice<KNET_CreditDeal::RiskChoice> knetNoRisk;
  //
  if ((psNoRisk&(1<<0))==(1<<0))
    knetNoRisk.set(KNET_EnquiryHeaderChange::KNET_RISK_CPTY);
  if ((psNoRisk&(1<<1))==(1<<1))
    knetNoRisk.set(KNET_EnquiryHeaderChange::KNET_RISK_COUNTRY);
  if ((psNoRisk&(1<<2))==(1<<2))
    knetNoRisk.set(KNET_EnquiryHeaderChange::KNET_RISK_INDUSTRY);
  if ((psNoRisk&(1<<3))==(1<<3))
    knetNoRisk.set(KNET_EnquiryHeaderChange::KNET_RISK_CREDIT);
  if ((psNoRisk&(1<<4))==(1<<4))
    knetNoRisk.set(KNET_EnquiryHeaderChange::KNET_RISK_SETTLEMENT);
  if ((psNoRisk&(1<<5))==(1<<5))
    knetNoRisk.set(KNET_EnquiryHeaderChange::KNET_RISK_RATING);
  //
  return knetNoRisk;
}

KNET_DealHeaderChange::TrialChoice
KNCB_CreditLimit::PSToKNETHasDoneTrial(PS_String_var const& psHasDoneTrial)
{
  if (!strcmp(psHasDoneTrial,"O"))
    return KNET_DealHeaderChange::KNET_TRIAL_NONE;
  else if (!strcmp(psHasDoneTrial,"Y"))
    return KNET_DealHeaderChange::KNET_TRIAL_DONE;
  else if (!strcmp(psHasDoneTrial,"W"))
    return KNET_DealHeaderChange::KNET_TRIAL_WITH_EXCESS;
  assert(!"KNCB_CreditLimit::PSToKNETHasDoneTrial mismatch");
  return KNET_DealHeaderChange::KNET_TRIAL_NONE;
}


KGR_MultiChoice<KNET_CreditDeal::GuaranteeType>
KNCB_CreditLimit::PSToKNETGuaranteeType(long psGuaranteeType)
{
  KGR_MultiChoice<KNET_CreditDeal::GuaranteeType> knetGuaranteeType;
  //
  if ((psGuaranteeType&(1<<0))==(1<<0))
    knetGuaranteeType.set(KNET_CreditDeal::KNET_GUARANTEE_TYPE_CPTY);
  if ((psGuaranteeType&(1<<1))==(1<<1))
    knetGuaranteeType.set(KNET_CreditDeal::KNET_GUARANTEE_TYPE_SOVEREIGN);
  if ((psGuaranteeType&(1<<2))==(1<<2))
    knetGuaranteeType.set(KNET_CreditDeal::KNET_GUARANTEE_TYPE_INDUSTRY);
  //
  return knetGuaranteeType;
  knetGuaranteeType.set(KNET_CreditDeal::KNET_GUARANTEE_TYPE_CPTY);
}


KNET_LimitCoverageElement::CreditKind
KNCB_CreditLimit::PSToKNETCreditKind(PS_String_var const& psCreditKind)
{
  if (!strcmp(psCreditKind,"C"))
    return KNET_LimitCoverageElement::KNET_CPTY;
  else if (!strcmp(psCreditKind,"I"))
    return KNET_LimitCoverageElement::KNET_ISSUER;
  else if (!strcmp(psCreditKind,"G"))
    return KNET_LimitCoverageElement::KNET_GUARANTOR;
  assert(!"KNCB_CreditLimit::PSToKNETCreditKind mismatch");
  return KNET_LimitCoverageElement::KNET_CPTY;
}


KNET_Limit::RefMode
KNCB_CreditLimit::PSToKNETRefMode(PS_String_var const& psRefMode)
{
  if (!strcmp(psRefMode,"A"))
    return KNET_Limit::REF_MODE_ANY;
  else if (!strcmp(psRefMode,"H"))
    return KNET_Limit::REF_MODE_HIERARCHY;
  else if (!strcmp(psRefMode,"E"))
    return KNET_Limit::REF_MODE_ENTITY;
  assert(!"KNCB_CreditLimitCoverage::PSToKNETRefMode mismatch");
  return KNET_Limit::REF_MODE_ANY;
}


string
KNCB_CreditLimit::KNETToPSRefMode(KNET_Limit::RefMode knetRefMode)
{
  if (knetRefMode==KNET_Limit::REF_MODE_ANY)
    return string("A");
  else if (knetRefMode==KNET_Limit::REF_MODE_HIERARCHY)
    return string("H");
  else if (knetRefMode==KNET_Limit::REF_MODE_ENTITY)
    return string("E");
  assert(!"KNCB_CreditLimit::KNETToPSRefMode mismatch ");
  return string("A");
}


KNET_Limit::RefModeIG
KNCB_CreditLimit::PSToKNETRefModeIG(PS_String_var const& psRefMode)
{
  if (!strcmp(psRefMode,"A"))
    return KNET_Limit::REF_MODE_IG_ANY;
  else if (!strcmp(psRefMode,"N"))
    return KNET_Limit::REF_MODE_IG_ANY_INTRA_GROUP;
  else if (!strcmp(psRefMode,"Y"))
    return KNET_Limit::REF_MODE_IG_ANY_THIRD_PARTY;
  else if (!strcmp(psRefMode,"H"))
    return KNET_Limit::REF_MODE_IG_HIERARCHY;
  else if (!strcmp(psRefMode,"I"))
    return KNET_Limit::REF_MODE_IG_HIERARCHY_INTRA_GROUP;
  else if (!strcmp(psRefMode,"T"))
    return KNET_Limit::REF_MODE_IG_HIERARCHY_THIRD_PARTY;
  else if (!strcmp(psRefMode,"E"))
    return KNET_Limit::REF_MODE_IG_ENTITY;
  assert(!"KNCB_CreditLimitCoverage::PSToKNETRefModeIG mismatch");
  return KNET_Limit::REF_MODE_IG_ANY;
}


string
KNCB_CreditLimit::KNETToPSRefModeIG(KNET_Limit::RefModeIG knetRefMode)
{
  if (knetRefMode==KNET_Limit::REF_MODE_IG_ANY)
    return string("A");
  else if (knetRefMode==KNET_Limit::REF_MODE_IG_ANY_INTRA_GROUP)
    return string("N");
  else if (knetRefMode==KNET_Limit::REF_MODE_IG_ANY_THIRD_PARTY)
    return string("Y");
  else if (knetRefMode==KNET_Limit::REF_MODE_IG_HIERARCHY)
    return string("H");
  else if (knetRefMode==KNET_Limit::REF_MODE_IG_HIERARCHY_INTRA_GROUP)
    return string("I");
  else if (knetRefMode==KNET_Limit::REF_MODE_IG_HIERARCHY_THIRD_PARTY)
    return string("T");
  else if (knetRefMode==KNET_Limit::REF_MODE_IG_ENTITY)
    return string("E");
  assert(!"KNCB_CreditLimit::KNETToPSRefModeIG mismatch ");
  return string("A");
}


KNET_LimitAvailability::SovereignKind
KNCB_CreditLimit::PSToKNETSovereignKind(PS_String_var const& psSovereignKind)
{
  if (!strcmp(psSovereignKind,"N"))
    return KNET_LimitAvailability::KNET_NONE_KIND;
  else if (!strcmp(psSovereignKind,"D"))
    return KNET_LimitAvailability::KNET_DOMESTIC_KIND;
  else if (!strcmp(psSovereignKind,"U"))
    return KNET_LimitAvailability::KNET_ULTIMATE_KIND;
  else if (!strcmp(psSovereignKind,"B"))
    return KNET_LimitAvailability::KNET_BOTH_KIND;
  else if (!strcmp(psSovereignKind,"C"))
    return KNET_LimitAvailability::KNET_CROSS_BORDER_KIND;
  assert(!"KNCB_CreditLimit::PSToKNETSovereignKind mismatch");
  return KNET_LimitAvailability::KNET_NONE_KIND;
}

string
KNCB_CreditLimit::KNETToPSSovereignKind(KNET_LimitAvailability::SovereignKind knetSovereignKind)
{
  if (knetSovereignKind==KNET_LimitAvailability::KNET_NONE_KIND)
    return string("N");
  else if (knetSovereignKind==KNET_LimitAvailability::KNET_DOMESTIC_KIND)
    return string("D");
  else if (knetSovereignKind==KNET_LimitAvailability::KNET_ULTIMATE_KIND)
    return string("U");
  else if (knetSovereignKind==KNET_LimitAvailability::KNET_BOTH_KIND)
    return string("B");
  else if (knetSovereignKind==KNET_LimitAvailability::KNET_CROSS_BORDER_KIND)
    return string("C");
  assert(!"KNCB_CreditLimit::KNETToPSSovereignKind mismatch");
  return string("N");
}


KNET_LimitAvailability::OverdraftMode
KNCB_CreditLimit::PSToKNETOverdraftMode(PS_String_var const& psOverdraftMode)
{
  if (!strcmp(psOverdraftMode,"N"))
    return KNET_LimitAvailability::KNET_OVERDRAFT_MODE_NONE;
  else if (!strcmp(psOverdraftMode,"D"))
    return KNET_LimitAvailability::KNET_OVERDRAFT_MODE_DEAL;
  else if (!strcmp(psOverdraftMode,"B"))
    return KNET_LimitAvailability::KNET_OVERDRAFT_MODE_BATCH;
  else if (!strcmp(psOverdraftMode,"T"))
    return KNET_LimitAvailability::KNET_OVERDRAFT_MODE_TIME;
  else if (!strcmp(psOverdraftMode,"L"))
    return KNET_LimitAvailability::KNET_OVERDRAFT_MODE_LOCKED;
  else if (!strcmp(psOverdraftMode,"O"))
    return KNET_LimitAvailability::KNET_OVERDRAFT_MODE_LOCK;
  else if (!strcmp(psOverdraftMode,"U"))
    return KNET_LimitAvailability::KNET_OVERDRAFT_MODE_UNDER_USED;
  else if (!strcmp(psOverdraftMode,"A"))
    return KNET_LimitAvailability::KNET_OVERDRAFT_MODE_ALMOST_EXCEEDED;
  else if (!strcmp(psOverdraftMode,"S"))
    return KNET_LimitAvailability::KNET_OVERDRAFT_MODE_SMALL_EXCESS;
  else if (!strcmp(psOverdraftMode,"V"))
    return KNET_LimitAvailability::KNET_OVERDRAFT_MODE_RESERVATION_EXCESS;
  else if (!strcmp(psOverdraftMode,"I"))
    return KNET_LimitAvailability::KNET_OVERDRAFT_MODE_VALIDATION;
  assert(!"KNCB_CreditLimit::PSToKNETOverdraftMode mismatch");
  return KNET_LimitAvailability::KNET_OVERDRAFT_MODE_NONE;
}


string
KNCB_CreditLimit::KNETToPSOverdraftMode(KNET_LimitAvailability::OverdraftMode knetOverdraftMode)
{
  if (knetOverdraftMode==KNET_LimitAvailability::KNET_OVERDRAFT_MODE_NONE)
    return string("N");
  else if (knetOverdraftMode==KNET_LimitAvailability::KNET_OVERDRAFT_MODE_DEAL)
    return string("D");
  else if (knetOverdraftMode==KNET_LimitAvailability::KNET_OVERDRAFT_MODE_BATCH)
    return string("B");
  else if (knetOverdraftMode==KNET_LimitAvailability::KNET_OVERDRAFT_MODE_TIME)
    return string("T");
  else if (knetOverdraftMode==KNET_LimitAvailability::KNET_OVERDRAFT_MODE_LOCKED)
    return string("L");
  else if (knetOverdraftMode==KNET_LimitAvailability::KNET_OVERDRAFT_MODE_LOCK)
    return string("O");
  else if (knetOverdraftMode==KNET_LimitAvailability::KNET_OVERDRAFT_MODE_UNDER_USED)
    return string("U");
  else if (knetOverdraftMode==KNET_LimitAvailability::KNET_OVERDRAFT_MODE_ALMOST_EXCEEDED)
    return string("A");
  else if (knetOverdraftMode==KNET_LimitAvailability::KNET_OVERDRAFT_MODE_SMALL_EXCESS)
    return string("S");
  else if (knetOverdraftMode==KNET_LimitAvailability::KNET_OVERDRAFT_MODE_RESERVATION_EXCESS)
    return string("V");
  else if (knetOverdraftMode==KNET_LimitAvailability::KNET_OVERDRAFT_MODE_VALIDATION)
    return string("I");
  assert(!"KNCB_CreditLimit::PSToKNETOverdraftMode mismatch");
  return string("N");
}


KNET_Setup::CreditMethod
KNCB_CreditLimit::PSToKNETCreditMethod(PS_String_var const& psCreditMethod)
{
  if (!strcmp(psCreditMethod,"S"))
    return KNET_Setup::KNET_SIMPLE;
  else if (!strcmp(psCreditMethod,"R"))
    return KNET_Setup::KNET_RUSSIAN_DOLL;
  else if (!strcmp(psCreditMethod,"I"))
    return KNET_Setup::KNET_INVERTED_RUSSIAN_DOLL;
  else if (!strcmp(psCreditMethod,"E"))
    return KNET_Setup::KNET_EXACT_DATED_IMPACT;
  assert(!"KNCB_CreditLimit::PSToKNETCreditMethod mismatch");
  return KNET_Setup::KNET_SIMPLE;
}


string
KNCB_CreditLimit::KNETToPSCreditMethod(KNET_Setup::CreditMethod knetCreditMethod)
{
  if (knetCreditMethod==KNET_Setup::KNET_SIMPLE)
    return string("S");
  else if (knetCreditMethod==KNET_Setup::KNET_RUSSIAN_DOLL)
    return string("R");
  else if (knetCreditMethod==KNET_Setup::KNET_INVERTED_RUSSIAN_DOLL)
    return string("I");
  else if (knetCreditMethod==KNET_Setup::KNET_EXACT_DATED_IMPACT)
    return string("E");
  assert(!"KNCB_CreditLimit::KNETToPSCreditMethod mismatch");
  return string("S");
}


KNET_Limit::LimitKind KNCB_CreditLimit::PSToKNETLimitKind(PS_String_var const& psLimitKind)
{
  if (!strcmp(psLimitKind,"S"))
    return KNET_Limit::LIMIT_KIND_STANDARD;
  else if (!strcmp(psLimitKind,"B"))
    return KNET_Limit::LIMIT_KIND_BLACK_HOLE;
  else if (!strcmp(psLimitKind,"C"))
    return KNET_Limit::LIMIT_KIND_CONCENTRATION_CAPS;

  assert(!"KNCB_CreditLimit::PSToKNETLimitKind mismatch");
  return KNET_Limit::LIMIT_KIND_STANDARD;
}


string KNCB_CreditLimit::KNETToPSLimitKind(KNET_Limit::LimitKind knetLimitKind)
{
  if (knetLimitKind==KNET_Limit::LIMIT_KIND_STANDARD)
    return string("S");
  else if (knetLimitKind==KNET_Limit::LIMIT_KIND_BLACK_HOLE)
    return string("B");
  else if (knetLimitKind==KNET_Limit::LIMIT_KIND_CONCENTRATION_CAPS)
    return string("C");

  assert(!"KNCB_CreditLimit::KNETToPSLimitKind mismatch");
  return string("S");
}

void KNCB_CreditLimit::PSToKNET(TimeBandCoverageElt_var const &psData,
                                KGL_TimeBandCoverageElementAccess &knetData )
{
    KNET_Identity TBIdentity =
        getIdentity( psData->arcTimeBand() );
	if ( psData->MsgNULL())
        knetData.setMessageNULL();
    else{
    	string s = psData->Msg().buff() ;
    	if(s.empty()){
    		knetData.setMessageNULL();
    	}
    	else{
    		knetData.setMessage( psData->Msg());
    	}
    }


    knetData.setAllocatedAmount( psData->AllocatedAmount() );

    //used amount for the single time band

    KGLDB_WhereClause whereClause;
    whereClause.erase();
    whereClause.addCondition( "CreditLimitMasterId", "=", psData->CreditLimitMasterId() );
    whereClause.addCondition( "TimeBandId", "=", psData->TimeBandId() );

    CreditLimit_Cltn_var CLColl = CreditLimit_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());
    if(!PS_is_nil(CLColl) && 0 != CLColl->length() )
    {
		CreditLimit_var psCreditLimitSource = CLColl[ 0ul ] ;
		// Used Amounts
		knetData.setUsedAmount(psCreditLimitSource->UsedAmount());
		knetData.setUsedAmountWoNet(psCreditLimitSource->UsedAmount_WoNet());
		if(!psCreditLimitSource->UsedAmount_MCNULL())
			knetData.setUsedAmountMC(psCreditLimitSource->UsedAmount_MC());
		if(!psCreditLimitSource->UsedAmount_MCNetNULL())
			knetData.setUsedAmountMCNet(psCreditLimitSource->UsedAmount_MCNet());
		if(!psCreditLimitSource->UsedAmount_MCNetCollatNULL())
			knetData.setUsedAmountMCNetCollat(psCreditLimitSource->UsedAmount_MCNetCollat());
    }
    else
    {
		//throw_NOTFOUND(CreditLimit_Factory::instance()->className());
		knetData.setUsedAmount(0.0);
		knetData.setUsedAmountWoNet(0.0);
		// maybe should test useExternalRiskEngine and productExposureMC before setting values below..
		knetData.setUsedAmountMC(0.0);
		knetData.setUsedAmountMCNet(0.0);
		knetData.setUsedAmountMCNetCollat(0.0);
    }


    knetData.setIsEligible( psData->IsTransferEligible() );
    knetData.setTimeBand( TBIdentity );

    //in each time we may have an allocation schedule defined

    CreditTBAllocSchedElt_Cltn_var collASElts =
		CreditTBAllocSchedElt_Factory::instance()->querySQLWhere( whereClause.getConditions().c_str() );

    KGR_Collection< KGL_AllocationSchedule > TBSchedules;

    
    for( unsigned long j = 0; j < collASElts->length(); ++j )
    {
		KGL_AllocationSchedule TBallocationScheduleData;

		TBallocationScheduleData.setBeginDate( PSToKGR_Date( collASElts[j]->BeginDate() ) );
		TBallocationScheduleData.setEndDate( PSToKGR_Date( collASElts[j]->EndDate() ) );
		TBallocationScheduleData.setAllocation( collASElts[j]->Allocation() );

		TBSchedules.push_back(TBallocationScheduleData);
    }

    knetData.setAllocationSchedule( TBSchedules );
}

struct sortByTimeBandLowBoudary
{
	bool operator() (TBElt const &tb1,
					 TBElt const &tb2)
		{
			return tb1.tb_->NoDays_Low() < tb2.tb_->NoDays_Low();
		}
};


void KNCB_CreditLimit::PSBaseToKNET( CreditLimitMasterBase const &base,
                                     RELATED_KNET_CLASS_ACCESS   &knetData )
{
	KGR_Id dataId( base.Id()->getOidVal() );

	// mandatory fields
	knetData.setId( dataId );
	knetData.setCurrency( getIdentity( base.arcCurrency() ) );
	//allocated amount of the whole limit master
	knetData.setAllocatedAmount( base.AllocatedAmount() );

	knetData.setAllocationDate( PSTotime_t( base.AllocationDate() ) );
	knetData.setFullMaturity( base.FullMaturity() );
	knetData.setCreditMethod( PSToKNETCreditMethod( base.CreditMethod() ) );
	knetData.setLocked( base.Locked() );
	knetData.setImpactBatchOnly( base.BatchOnly() );
	knetData.setUseTimeBand( base.UseTimeBand() );
	knetData.setHasSchedule( base.HasSchedule() );
	knetData.setAutomaticAllocTransfer( base.AutomaticAllocationTransfert() );
	knetData.setShortName( base.ShortName() );
	knetData.setName( base.Name() );
	knetData.setUseValueDateReview( base.UseVDV() );
	knetData.setIsEntity( base.IsEntity() );
	knetData.setLimitGroup( base.LimitGroup() );

	// NULL allowed attributes
	if( base.EndDateNULL() )
		knetData.setEndDateNULL();
	else
		knetData.setEndDate( PSToKGR_Date( base.EndDate() ) );

	if( base.BeginDateNULL() )
		knetData.setBeginDateNULL();
	else
		knetData.setBeginDate( PSToKGR_Date( base.BeginDate() ) );

	if( base.LockDateNULL() )
		knetData.setLockDateNULL();
	else
		knetData.setLockDate( PSToKGR_Date( base.LockDate() ) );

	if( base.EnforcedNULL() )
		knetData.setEnforcedNULL();
	else
		knetData.setEnforced( base.Enforced() );

	if( base.AnnotationNULL() )
		knetData.setAnnotationNULL();
	else
		knetData.setAnnotation( base.Annotation() );

  //Fix for 00012487.KRE : Limit double validation does not work for limit reviewer
    if( base.ReviewerIdNULL() )
        knetData.setLimitReviewerNULL();
    else
        knetData.setLimitReviewer( getIdentity( base.arcReviewer() ) );

	if( base.MsgNULL()){
		knetData.setMessageNULL();
	}
	else {
		string s = base.Msg().buff() ;
		if(s.empty()){
			knetData.setMessageNULL();
		}
		else{
			knetData.setMessage( base.Msg() );
		}
	}


	if( base.MessageOnLockNULL() )
		knetData.setMessageOnLockNULL();
	else{
		string s = base.MessageOnLock().buff() ;
		if(s.empty()){
			knetData.setMessageOnLockNULL();
		}
		else{
			knetData.setMessageOnLock( base.MessageOnLock());
		}
	}


	if( base.AmountTypeNULL() )
		knetData.setAmountTypeNULL();
	else
		knetData.setAmountType(KNDBC_ConvChoice::Ps2KNET_AmountType( base.AmountType().buff()[0] ) );

	//create TB message model here Karim Sebbah
	KGLDB_WhereClause whereClause;
	whereClause.addCondition( "CreditLimitMasterId", "=", base.Id() );

	TimeBandCoverageElt_Cltn_var collTimeBandElts =
		TimeBandCoverageElt_Factory::instance()->querySQLWhere( whereClause.getConditions().c_str() );

	KGR_Collection< KGL_TimeBandCoverageElementAccess > timeBandCoverageElement;
	std::vector<TBElt> tmpColl;
	TBElt elt;
	KGL_TimeBandCoverageElementAccess timeBandElt;
	TimeBandCoverageElt_var tbcElt;
	TimeBand_var tb;
	for( unsigned long k=0; k<collTimeBandElts->length(); ++k )
	{
		tbcElt = collTimeBandElts[k];
		// get the TB.
		tb = tbcElt->arcTimeBand();
		if (PS_is_nil(tb)) continue;
		// create a new elt to push in the vector to be sorted
		elt.tb_    = tb ;
		elt.TBElt_ = tbcElt ;
		tmpColl.push_back( elt );
	}
	// sort the vector.
	std::sort( tmpColl.begin(), tmpColl.end(), sortByTimeBandLowBoudary() );

	for( unsigned long l=0; l<tmpColl.size(); ++l )
	{
		KGL_TimeBandCoverageElementAccess timeBandElt;
		PSToKNET( tmpColl[l].TBElt_, timeBandElt );
		timeBandCoverageElement.push_back( timeBandElt );
	}

	knetData.setTimeBandCoverageElement( timeBandCoverageElement );


	KGLDB_WhereClause whereClause2;
	whereClause2.addCondition( "CreditLimitMasterId", "=", base.Id() );

	ReviewCredElt_Cltn_var cltnReviewDate =
		ReviewCredElt_Factory::instance()->querySQLWhere( whereClause2.getConditions().c_str() );

	KGR_Collection< KGL_ReviewDate > reviewDates;

	
	for( unsigned long i = 0; i < cltnReviewDate->length(); ++i )
    {
		KGL_ReviewDate reviewDateData;

		reviewDateData.setReviewDate( PSToKGR_Date(cltnReviewDate[i]->ReviewDate()) );
		reviewDateData.setMessage( cltnReviewDate[i]->Msg() );
		reviewDateData.setComment( cltnReviewDate[i]->Annotation() );

		reviewDates.push_back( reviewDateData );
    }

	knetData.setReviewDates( reviewDates );


	CreditAllocSchedElt_Cltn_var cltnAllocationSchedule =
		CreditAllocSchedElt_Factory::instance()->querySQLWhere(whereClause2.getConditions().c_str());

	KGR_Collection< KGL_AllocationSchedule > schedules;

	
	for( unsigned long j = 0; j < cltnAllocationSchedule->length(); j++ )
    {
		KGL_AllocationSchedule allocationScheduleData;

		allocationScheduleData.setBeginDate( PSToKGR_Date( cltnAllocationSchedule[j]->BeginDate() ) );
		allocationScheduleData.setEndDate( PSToKGR_Date( cltnAllocationSchedule[j]->EndDate() ) );
		allocationScheduleData.setAllocation( cltnAllocationSchedule[j]->Allocation() );

		schedules.push_back( allocationScheduleData );
    }

	knetData.setAllocationSchedule( schedules );
}


void KNCB_CreditLimit::PSCovToKNET( CLMasterDVCoverage const  &base,
                                    RELATED_KNET_CLASS_ACCESS &knetData )
{
  // fill in CreditLimitMasterBase related fields
  PSBaseToKNET( base, knetData );


  // mandatory fields
  knetData.setCptyRefMode(PSToKNETRefModeIG(base.RefMode_Cpty()));
  knetData.setIndustryRefMode(PSToKNETRefMode(base.RefMode_Industry()));
  knetData.setInstrumentRefMode(PSToKNETRefMode(base.RefMode_Instrument()));
  knetData.setCountryRefMode(PSToKNETRefMode(base.RefMode_Country()));
  knetData.setFolderRefMode(PSToKNETRefMode(base.RefMode_Folder()));
  knetData.setCurrencyRefMode(PSToKNETRefMode(base.RefMode_Currency()));
  knetData.setUserRefMode(PSToKNETRefMode(base.RefMode_KNUser()));
  knetData.setProjectRefMode(PSToKNETRefMode(base.RefMode_KGRProject()));
  knetData.setSovereignKind(PSToKNETSovereignKind(base.SovereignKind()));
  knetData.setLimitKind( PSToKNETLimitKind( base.LimitKind() ) );
  knetData.setStatus( KNCBTK_DVTool::PSToKNETStatus( base.getStatus() ) );
  knetData.setCapitalLimit( base.CapitalLimit() );
  knetData.setStatus( KNCBTK_DVTool::PSToKNETStatus( base.Status() ) );

  knetData.setEconomicCapitalLimit( base.EconomicCapitalLimit() );
  knetData.setUseTimeBand(  base.UseTimeBand()  );
  // NULL allowed fields
  if( base.CreditLimitCoverageIdNULL() )
    knetData.setLimitCoverageNULL(  );
  else
    knetData.setLimitCoverage( getIdentity( base.arcCreditLimitCoverage() ) );

 
  if( base.RiskWeightCoverageIdNULL() )
    knetData.setRiskWeightCoverageNULL();
  else
    knetData.setRiskWeightCoverage( getIdentity( base.arcRiskWeightCoverage() ) );

  if( base.CptyId_CoverageNULL() )
    knetData.setCptyCoverageNULL();
  else
    knetData.setCptyCoverage( getIdentity( base.arcCptyCoverage() ) );

  if( base.IndustryId_CoverageNULL() )
    knetData.setIndustryCoverageNULL();
  else
    knetData.setIndustryCoverage( getIdentity( base.arcIndustryCoverage() ) );

  if( base.InstrumentId_CoverageNULL() )
    knetData.setInstrumentCoverageNULL();
  else
    knetData.setInstrumentCoverage( getIdentity( base.arcInstrumentCoverage() ) );

  if( base.CountryId_CoverageNULL() )
    knetData.setCountryCoverageNULL();
  else
    knetData.setCountryCoverage( getIdentity( base.arcCountryCoverage() ) );

  if( base.FolderId_CoverageNULL() )
    knetData.setFolderCoverageNULL();
  else
    knetData.setFolderCoverage( getIdentity( base.arcFolderCoverage() ) );

  if( base.CurrencyId_CoverageNULL() )
    knetData.setCurrencyCoverageNULL();
  else
    knetData.setCurrencyCoverage( getIdentity( base.arcCurrencyCoverage() ) );

  if( base.KNUserId_CoverageNULL() )
    knetData.setUserCoverageNULL();
  else
    knetData.setUserCoverage( getIdentity( base.arcKNUserCoverage() ) );

  if( base.RatingId_CoverageNULL() )
    knetData.setRatingCoverageNULL();
  else
    knetData.setRatingCoverage( getIdentity( base.arcRatingCoverage() ) );

  if( base.RatingAgencyIdNULL() )
    knetData.setRatingAgencyCoverageNULL();
  else
    knetData.setRatingAgencyCoverage( getIdentity( base.arcRatingAgency() ) );

  if( base.ValidationRequestingUserIdNULL() )
    knetData.setRequestingUserNULL();
  else
    knetData.setRequestingUser( getIdentity( base.arcValidationRqstngUser() ) );

  if( base.ValidationRequestDateNULL() )
    knetData.setRequestingDateNULL();
  else
    knetData.setRequestingDate( PSToKGR_Date( base.ValidationRequestDate() ) );

  if( base.KGRProjectId_CoverageNULL() )
    knetData.setProjectCoverageNULL();
  else
    knetData.setProjectCoverage(getIdentity( base.arcKGRProjectCoverage() ) );

  if( base.ReviewerIdNULL() )
    knetData.setLimitReviewerNULL();
  else
    {
      KNUser_var psLimitReviewer
      = KNUser_Factory::instance()->queryKey( *base.ReviewerId(),
                                              PS_Defs::k_cacheThenDatabase );
      knetData.setLimitReviewer(KNCBTK_IdentityTool<KNUser_var,
                                KNUser_Factory,
                                KNUser_Iter_var,
                                KNUser_Cltn_var>
                                ::getIdentity(psLimitReviewer, base.ReviewerId()));
    }



}


void KNCB_CreditLimit::PSToKNET( RELATED_PS_COV_CLASS_VAR const &object,
                                 RELATED_KNET_CLASS_ACCESS      &knetCreditLimit )
{
  if( strcmp( object->className().buff(),
              RELATED_PS_FACTORY::instance()->className() ) == 0 )
    PSToKNET( RELATED_PS_CLASS_VAR::narrow( object ), knetCreditLimit );
  else
    PSCovToKNET( *object, knetCreditLimit );
}


void KNCB_CreditLimit::PSToKNET( RELATED_PS_CLASS_VAR const &object,
                                 RELATED_KNET_CLASS_ACCESS  &knetCreditLimit )
{
	// usedAmount n'est plus dans la credit limit master mais dans la credit limit
	// overDraftMode n'est plus dans la credit limit master mais dans la credit limit

	// filling in fields related to CLMasterDVCov table
	PSCovToKNET( *object, knetCreditLimit );


	// we fill right here the used amount if and only if it is an infinite limite
	KGLDB_WhereClause whereClause;
	whereClause.addCondition( "CreditLimitMasterId", "=", object->Id() );

	TimeBandCoverageElt_Cltn_var collTimeBandElts =
		TimeBandCoverageElt_Factory::instance()->querySQLWhere( whereClause.getConditions().c_str() );


	if(collTimeBandElts->length()==0)	//case infinite limite, the TB element is also the master limit
    {
		whereClause.erase();
		whereClause.addCondition( "CreditLimitMasterId", "=", object->Id() );
		whereClause.addCondition( "TimeBandId", "=", object->TimeBandId() );

		CreditLimit_Cltn_var CLColl = CreditLimit_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());
		if(!PS_is_nil(CLColl) &&  0 != CLColl->length())
        {
			CreditLimit_var psCreditLimitSource = CLColl[ 0ul ];
			knetCreditLimit.setUsedAmount(psCreditLimitSource->UsedAmount());

			if(!psCreditLimitSource->UsedAmount_MCNULL())
				knetCreditLimit.setUsedAmountMC(psCreditLimitSource->UsedAmount_MC());

			if(!psCreditLimitSource->UsedAmount_MCNetNULL())
				knetCreditLimit.setUsedAmountMCNet(psCreditLimitSource->UsedAmount_MCNet());

			if(!psCreditLimitSource->UsedAmount_MCNetCollatNULL())
				knetCreditLimit.setUsedAmountMCNetCollat(psCreditLimitSource->UsedAmount_MCNetCollat());

			if(!psCreditLimitSource->UsedAmount_WoNetNULL())
				knetCreditLimit.setUsedAmountWoNet(psCreditLimitSource->UsedAmount_WoNet());

			//we set the time band infinite
			TimeBand_var psTimeBand = TimeBand_Factory::instance()->queryName( INFINIT_TB_SHORTNAME );

			knetCreditLimit.setTimeBand (KNET_Identity(psTimeBand->ShortName()
													   ,psTimeBand->Name()
													   ,KGR_Id(psTimeBand->Id()->getOidVal())));


        }
		else
        {
			knetCreditLimit.setUsedAmount(0.0);
			TimeBand_var psTimeBand = TimeBand_Factory::instance()->queryName( INFINIT_TB_SHORTNAME );

			knetCreditLimit.setTimeBand (KNET_Identity(psTimeBand->ShortName()
													   ,psTimeBand->Name()
													   ,KGR_Id(psTimeBand->Id()->getOidVal())));

			//throw_NOTFOUND(CreditLimit_Factory::instance()->className());
        }
    }
	else // the master has time bands
	{
		KGR_Collection< KGL_TimeBandCoverageElementAccess > timeBandCoverageElement;

		std::vector<TBElt> tmpColl;
		TBElt elt;
		KGL_TimeBandCoverageElementAccess timeBandElt;
		TimeBandCoverageElt_var tbcElt;
		TimeBand_var tb;
		for( unsigned long l=0; l<collTimeBandElts->length(); ++l )
		{
			tbcElt = collTimeBandElts[l];
			// get the TB.
			tb = tbcElt->arcTimeBand();
			if (PS_is_nil(tb)) continue;
			// create a new elt to push in the vector to be sorted
			elt.tb_    = tb ;
			elt.TBElt_ = tbcElt ;
			tmpColl.push_back( elt );
		}
		// sort the vector.
		std::sort( tmpColl.begin(), tmpColl.end(), sortByTimeBandLowBoudary() );

		for( unsigned long k=0; k<tmpColl.size(); ++k )
		{
			KGL_TimeBandCoverageElementAccess timeBandElt;
			PSToKNET(tmpColl[k].TBElt_, timeBandElt);
			timeBandCoverageElement.push_back( timeBandElt );
		}
		knetCreditLimit.setTimeBandCoverageElement( timeBandCoverageElement );
	}

	// mandatory fields
	knetCreditLimit.setLastReviewDate(PSToKGR_Date(object->LastReviewDate()));


	// NULL allowed fields
	if( object->ApprovingUserIdNULL() )
		knetCreditLimit.setApprovingUserNULL();
	else
		knetCreditLimit.setApprovingUser( getIdentity( object->arcValidationApvlUser() ) );

	if( object->ApprovalDateNULL() )
		knetCreditLimit.setApprovingDateNULL();
	else
		knetCreditLimit.setApprovingDate( PSToKGR_Date( object->ApprovalDate() ) );
	
	//Manage ValidationRequest  
	knetCreditLimit.setStatus( KNC_ConvChoice::Ps2KNET_ValidationStatus( object->Status()[0] ) );
	
        if( object->ValidationRequestingUserIdNULL()     )  
             knetCreditLimit.setRequestingUserNULL();  
        else  
             knetCreditLimit.setRequestingUser( getIdentity( object->arcValidationRqstngUser() ) );  
     
        if( object->ValidationRequestDateNULL())  
             knetCreditLimit.setRequestingDateNULL();  
        else  
             knetCreditLimit.setRequestingDate( PSToKGR_Date( object->ValidationRequestDate() ) );  

	if( object->NextReviewDateNULL() )
		knetCreditLimit.setNextReviewDateNULL();
	else
		knetCreditLimit.setNextReviewDate(PSToKGR_Date( object->NextReviewDate()) );

	if( object->ReviewerIdNULL() )
		knetCreditLimit.setLimitReviewerNULL();
	else
		knetCreditLimit.setLimitReviewer( getIdentity( object->arcReviewer() ) );
}


void KNCB_CreditLimit::setNameAndShortName( CreditLimitMasterBase        &object,
    KNET_CreditLimitChange const &data )
{
	string producedLabel;

	char limitGroup[20];

	bool set=false;
	bool set1=false;

	if( strcmp( "", data.getShortName() ) != 0 )
    {
		object.ShortName( data.getShortName() );

		//to fill limitGroup
		strcpy(limitGroup,data.getShortName());

		if(strcmp( "", data.getName() ) == 0)
        {
			object.Name( data.getShortName() );
			std_const_cast(KNET_CreditLimitChange &)(data).setName( data.getShortName() );

			set = true ;
        }
    }
	else
    {
		bool found = false;
		while( ! found )
        {
			producedLabel = KNTC_Tools::getDealNumber();

			KGLDB_WhereClause whereClause;
			whereClause.addCondition( "ShortName", "=", producedLabel.c_str() );

			CreditLimitMasterBase_Cltn_var iterSN
				= CreditLimitMasterBase_Factory::instance()->querySQLWhere( whereClause.getConditions().c_str() );

			if( PS_is_nil(iterSN) || 0==iterSN->length() )
            {
				found = true;
				object.ShortName( producedLabel.c_str() );

				//to fill limitGroup
				strcpy(limitGroup,producedLabel.c_str());

				std_const_cast(KNET_CreditLimitChange &)(data).setShortName( producedLabel.c_str() );
				set1=true;
            }
        }
    }


	if( strcmp( "", data.getName() ) != 0 )
    {
		object.Name( data.getName() );

		if(set1)
        {
			object.ShortName( data.getName() );

			//to fill limitGroup
			strcpy(limitGroup,data.getName());

			std_const_cast(KNET_CreditLimitChange &)(data).setShortName( data.getName() );
        }
    }
	else if(!set
		)
    {
		bool found = false;

		while( ! found )
        {
			if( producedLabel.size() == 0 )
				producedLabel = KNTC_Tools::getDealNumber();

			KGLDB_WhereClause whereClause;
			whereClause.addCondition( "Name", "=", producedLabel.c_str() );

			CreditLimitMasterBase_Cltn_var iterN
				= CreditLimitMasterBase_Factory::instance()->querySQLWhere( whereClause.getConditions().c_str() );

			if( iterN->length() > 0 )
            {
				found         = false;

				producedLabel = KNTC_Tools::getDealNumber();
            }
			else
            {
				found = true;
				object.Name( producedLabel.c_str() );
				std_const_cast(KNET_CreditLimitChange &)(data).setName( producedLabel.c_str() );
            }
        }
    }

	//if it is a limit group, limitGroup DB field has
	if(!data.getIsEntity())
	{
		object.LimitGroup(limitGroup);

	}

}


void KNCB_CreditLimit::isUpdateAcceptOkOrThrow( RELATED_PS_CLASS_VAR       previous,
    RELATED_PS_DELTA_CLASS_VAR next,
    KNET_RequestHandle         handle )
{
  RELATED_PS_CLASS_VAR tmpVar = RELATED_PS_CLASS_VAR::narrow( previous );

  if( PS_is_nil( tmpVar ) )
    throw_NOTFOUND( RELATED_PS_FACTORY::instance()->className() );

  if( !RELATED_PS_FACTORY::instance()->hasAccess( false, true, tmpVar,
      toPS( handle->getUser() ) ) )
    throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);

  if(!PS_is_nil(tmpVar->arcCptyCoverage()) &&
      !Cpty_Factory::instance()->hasAccess(2,false, true,tmpVar->arcCptyCoverage(),toPS( handle->getUser() )))
    {
      throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
    }
  if(!PS_is_nil(tmpVar->arcFolderCoverage()) &&
      !Folder_Factory::instance()->hasAccess(2,false, true,tmpVar->arcFolderCoverage(),toPS( handle->getUser() )))
    {
      throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
    }

}


void KNCB_CreditLimit::isUpdateRejectOkOrThrow( RELATED_PS_CLASS_VAR       previous,
    RELATED_PS_DELTA_CLASS_VAR next,
    KNET_RequestHandle         handle )
{
  RELATED_PS_CLASS_VAR tmpVar = RELATED_PS_CLASS_VAR::narrow( previous );

  if( PS_is_nil( tmpVar ) )
    throw_NOTFOUND( RELATED_PS_FACTORY::instance()->className() );

  if( !RELATED_PS_FACTORY::instance()->hasAccess( false, true, tmpVar,
      toPS( handle->getUser() ) ) )
    throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
  if(!PS_is_nil(tmpVar->arcCptyCoverage()) &&
      !Cpty_Factory::instance()->hasAccess(2,false, true,tmpVar->arcCptyCoverage(),toPS( handle->getUser() )))
    {
      throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
    }
  if(!PS_is_nil(tmpVar->arcFolderCoverage()) &&
      !Folder_Factory::instance()->hasAccess(2,false, true,tmpVar->arcFolderCoverage(),toPS( handle->getUser() )))
    {
      throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
    }
}


void KNCB_CreditLimit::isDeleteAcceptOkOrThrow( RELATED_PS_COV_CLASS_VAR doomed,
    KNET_RequestHandle       handle )
{
  RELATED_PS_CLASS_VAR tmpVar = RELATED_PS_CLASS_VAR::narrow( doomed );

  if( PS_is_nil( tmpVar ) )
    throw_NOTFOUND( RELATED_PS_FACTORY::instance()->className() );

  if( !RELATED_PS_FACTORY::instance()->hasAccess( false, true, tmpVar,
      toPS( handle->getUser() ) ) )
    throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
  if(!PS_is_nil(tmpVar->arcCptyCoverage()) &&
      !Cpty_Factory::instance()->hasAccess(2,false, true,tmpVar->arcCptyCoverage(),toPS( handle->getUser() )))
    {
      throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
    }
  if(!PS_is_nil(tmpVar->arcFolderCoverage()) &&
      !Folder_Factory::instance()->hasAccess(2,false, true,tmpVar->arcFolderCoverage(),toPS( handle->getUser() )))
    {
      throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
    }
}


void KNCB_CreditLimit::isDeleteRejectOkOrThrow( RELATED_PS_COV_CLASS_VAR doomed,
    KNET_RequestHandle       handle )
{
  RELATED_PS_CLASS_VAR tmpVar = RELATED_PS_CLASS_VAR::narrow( doomed );

  if( PS_is_nil( tmpVar ) )
    throw_NOTFOUND( RELATED_PS_FACTORY::instance()->className() );

  if( !RELATED_PS_FACTORY::instance()->hasAccess( false, true, tmpVar,
      toPS( handle->getUser() ) ) )
    throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
  if(!PS_is_nil(tmpVar->arcCptyCoverage()) &&
      !Cpty_Factory::instance()->hasAccess(2,false, true,tmpVar->arcCptyCoverage(),toPS( handle->getUser() )))
    {
      throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
    }
  if(!PS_is_nil(tmpVar->arcFolderCoverage()) &&
      !Folder_Factory::instance()->hasAccess(2,false, true,tmpVar->arcFolderCoverage(),toPS( handle->getUser() )))
    {
      throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
    }
}

void KNCB_CreditLimit::onRemoveFromDatabase(KGR_Id id)
{
	string limitIdStr = "0x" + KNC_ConvId::idToStr( id.getValue() );
	string condLog = "PurgeCreditLimitImpact ";
	condLog += limitIdStr;

	//PacketSize
	static const char* rowNumber = getenv( "ROWCOUNT_SIZE" );

	size_t rowNbParam = 0; //if 0, SP use 5000

	if(rowNumber && *rowNumber)
		rowNbParam = atoi(rowNumber);

	condLog += " , NULL, ";
	char 	buffer[10];
	sprintf(buffer, "%lu", rowNbParam);
	condLog += buffer;

	INFO_LOG << "Start PurgeCreditLimitImpact " << std::endl ;
	CreditLimitMaster_Cltn_var clmLogCltn = CreditLimitMaster_Factory::instance()->querySP(condLog.c_str());
	INFO_LOG << "End PurgeCreditLimitImpact " << std::endl ;
}

void KNCB_CreditLimit::KNETToPS( KNET_RequestHandle               handle,
                                 RELATED_KNET_CLASS_CHANGE const &knetData,
                                 RELATED_PS_CLASS_VAR            &object,
                                 bool                             setMandatoryAttributes )
{
  // no more overdraft mode nor used amount, both are linked to CreditLimit
  KGR_Id src( handle->getSource() );

  // set the DVCov related fields in this method
  KNETToCovPS( handle, knetData,
               std_static_cast( RELATED_PS_COV_CLASS_VAR )( object ),
               setMandatoryAttributes );

  // Then set the other ones

  // Mandatory attributes
  if( setMandatoryAttributes )
    {

      object->LastReviewDate(KNET_DateToPS(knetData.getLastReviewDate()).c_str());
      if( !RELATED_PS_FACTORY::instance()->hasAccess( false, true, object,
          toPS( handle->getUser() ) ) )
        throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
    }
  else
  {}
  if(!PS_is_nil(object->arcCptyCoverage()) &&
      !Cpty_Factory::instance()->hasAccess(2,false, true,object->arcCptyCoverage(),toPS( handle->getUser() )))
    {
      throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
    }
  if(!PS_is_nil(object->arcFolderCoverage()) &&
      !Folder_Factory::instance()->hasAccess(2,false, true,object->arcFolderCoverage(),toPS( handle->getUser() )))
    {
      throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
    }


  typedef RELATED_KNET_CLASS_CHANGE TP;
  typedef KNET_LimitChange          BT;
  BT const &base = knetData;

  object->arcReviewer( getVarOrNull<KNUser>( base, &BT::isLimitReviewerNULL,
                       &BT::getLimitReviewer, src ) );

}


void
KNCB_CreditLimit::createDefaultAccessRecords( KGR_Id const               &userId,
    CreditLimitMaster_var const &associatedData )
{
  AccessDefaultKNUser_Cltn_var coll;

  Setup_Cltn_var setupObject =
    Setup_Factory::instance()->allInstances( PS_Defs::k_cacheThenDatabase );

  if( setupObject[(unsigned long) 0]->ModeAccessConfig() )
    {
      KNUser_var psUser = getVar<KNUser>( userId );

      if( !PS_is_nil( psUser ) )
        coll = psUser->arcAccessData();
    }

  if( PS_is_nil( coll ) || coll->length() == 0 )
    AccessCreditLimitMaster_Factory::instance()->create( "G", 1, 1, associatedData );
  else
    {
	  unsigned long idx = 0;

      for( ; idx < coll->length(); ++idx )
        {
          if(coll[ (unsigned long) idx ]->AccessTypeCheck()&1)
            {
              AccessCreditLimitMaster_var access =
                AccessCreditLimitMaster_Factory::instance()->create(
                  coll[ (unsigned long) idx ]->AccessMode(),
                  coll[ (unsigned long) idx ]->AccessRightRead(),
                  coll[ (unsigned long) idx ]->AccessRightWrite(),
                  associatedData );

              access->arcKNUser( coll[ (unsigned long) idx ]->arcKNUser() );
            }
        }
    }
}


KNCB_CreditLimit::RELATED_PS_CLASS_VAR
KNCB_CreditLimit::dummyCreateFromKNET( KNET_RequestHandle               handle,
                                       RELATED_KNET_CLASS_CHANGE const &knetData,
                                       PS_Oid const                    *forcedId )
{

  string psStatus;
  psStatus = (char) KNDBC_Choices::VALIDATION_STATUS_ENABLE;

  string psSovereignKind     ( KNETToPSSovereignKind( knetData.getSovereignKind()) );
  string psLimitKind         ( KNETToPSLimitKind( knetData.getLimitKind()) );
  string psRefModeCpty       ( KNETToPSRefModeIG( knetData.getCptyRefMode()) );
  string psRefModeIndustry   ( KNETToPSRefMode( knetData.getIndustryRefMode()) );
  string psRefModeInstrument ( KNETToPSRefMode( knetData.getInstrumentRefMode()) );
  string psRefModeCountry    ( KNETToPSRefMode( knetData.getCountryRefMode()) );
  string psRefModeCurrency   ( KNETToPSRefMode( knetData.getCurrencyRefMode()) );
  string psRefModeFolder     ( KNETToPSRefMode( knetData.getFolderRefMode()) );
  string psRefModeKNUser     ( KNETToPSRefMode( knetData.getUserRefMode()) );
  string psRefModeProject    ( KNETToPSRefMode( knetData.getProjectRefMode()) );
  string psCreditMethod      ( KNETToPSCreditMethod( knetData.getCreditMethod()) );
  string psAllocationDate    ( time_tToPS( knetData.getAllocationDate()) );
  double psAllocatedAmount = knetData.getAllocatedAmount();
  short  psFullMaturity    = knetData.getFullMaturity();
  short  psLocked          = knetData.getLocked();
  short  psImpactBatchOnly = knetData.getImpactBatchOnly();

  // 0D-+ : a default value supposed to be allways available in the database
  TimeBand_var
  psTimeBand            = TimeBand_Factory::instance()->queryShortName( INFINIT_TB_SHORTNAME );
  Currency_var
  psCurrency            = getVar<Currency>( *knetData.getCurrency(),
                          handle->getSource() );
  RELATED_PS_CLASS_VAR object;

  // 	if( forcedId )
  // 	{
  // 		object = RELATED_PS_FACTORY::instance()->createWithOid( *forcedId,
  // 																psAllocatedAmount,
  // 																psAllocationDate.c_str(),
  // 																psFullMaturity,
  // 																psCreditMethod.c_str(),
  // 																psLocked,
  // 																psImpactBatchOnly,
  // 																knetData.getUseTimeBand(),
  // 																knetData.getHasSchedule(),
  // 																knetData.getAutomaticAllocTransfer(),
  // 																psRefModeCpty.c_str(),
  // 																psRefModeIndustry.c_str(),
  // 																psRefModeCountry.c_str(),
  // 																psSovereignKind.c_str(),
  // 																psRefModeFolder.c_str(),
  // 																psRefModeCurrency.c_str(),
  // 																psRefModeKNUser.c_str(),
  // 																psRefModeInstrument.c_str(),
  // 																psLimitKind.c_str(),
  // 																knetData.getCapitalLimit(),
  // 																psStatus.c_str(),
  // 																psTimeBand,
  // 																psCurrency );
  // 	}
  // 	else
  // 	{

  object = RELATED_PS_FACTORY::instance()->create( psAllocatedAmount,
           psAllocationDate.c_str(),
           psFullMaturity,
           psCreditMethod.c_str(),
           psLocked,
           psImpactBatchOnly,
           knetData.getUseTimeBand(),
           knetData.getHasSchedule(),
           knetData.getAutomaticAllocTransfer(),
           knetData.getUseValueDateReview(),
           knetData.getEconomicCapitalLimit(),
           knetData.getLimitGroup(),
           knetData.getIsEntity(),
           psRefModeCpty.c_str(),
           psRefModeIndustry.c_str(),
           psRefModeCountry.c_str(),
           psSovereignKind.c_str(),
           psRefModeFolder.c_str(),
           psRefModeCurrency.c_str(),
           psRefModeKNUser.c_str(),
           psRefModeInstrument.c_str(),
           psRefModeProject.c_str(),
           psLimitKind.c_str(),
           knetData.getCapitalLimit(),
           psStatus.c_str(),
           psCurrency );

	// to fill in non mandatory fields
	KNETToPS( handle, knetData, object, false );

	return object;
}


KNCB_CreditLimit::RELATED_PS_CLASS_VAR
KNCB_CreditLimit::createFromKNET( KNET_RequestHandle               handle,
                                  RELATED_KNET_CLASS_CHANGE const &knetData,
                                  PS_Oid const                    *forcedId )
{
  KNCB_CreditLimit::RELATED_PS_CLASS_VAR object =
    dummyCreateFromKNET( handle, knetData, forcedId );

  // then add Access related entries in the database
  createDefaultAccessRecords( handle->getUser(), object );

  return object;
}


KNCB_CreditLimit::RELATED_PS_INS_CLASS_VAR
KNCB_CreditLimit::createInsertProcessFromKNET( KNET_RequestHandle               handle,
    RELATED_KNET_CLASS_CHANGE const &knetData )
{

	KH_DBG::dbg("KNCB_CreditLimit::createInsertProcessFromKNET::method_start");
	char status[2] = { KNDBC_Choices::VALIDATION_STATUS_ENABLE, 0};

	string psSovereignKind(   KNETToPSSovereignKind( knetData.getSovereignKind()) );
	string psLimitKind(       KNETToPSLimitKind( knetData.getLimitKind()) );
	string psRefModeCpty(     KNETToPSRefModeIG( knetData.getCptyRefMode()) );
	string psRefModeIndustry( KNETToPSRefMode( knetData.getIndustryRefMode()) );
	string psRefModeInstrument( KNETToPSRefMode( knetData.getInstrumentRefMode()) );
	string psRefModeCountry(  KNETToPSRefMode( knetData.getCountryRefMode()) );
	string psRefModeCurrency( KNETToPSRefMode( knetData.getCurrencyRefMode()) );
	string psRefModeFolder(   KNETToPSRefMode( knetData.getFolderRefMode()) );
	string psRefModeKNUser(   KNETToPSRefMode( knetData.getUserRefMode()) );
	string psRefModeProject(  KNETToPSRefMode( knetData.getProjectRefMode()) );
	string psCreditMethod(    KNETToPSCreditMethod( knetData.getCreditMethod()) );
	string psAllocationDate(  time_tToPS( knetData.getAllocationDate()) );
	double psAllocatedAmount = knetData.getAllocatedAmount();
	short  psFullMaturity    = knetData.getFullMaturity();
	short  psLocked          = knetData.getLocked();
	short  psImpactBatchOnly = knetData.getImpactBatchOnly();

	// 0D-+ : a default value supposed to be always available in the database
	TimeBand_var
		psTimeBand            = TimeBand_Factory::instance()->queryShortName( INFINIT_TB_SHORTNAME );
	Currency_var
		psCurrency            = getVar<Currency>( *knetData.getCurrency(),
												  handle->getSource() );

	RELATED_PS_INS_CLASS_VAR object =
		CLMasterDVInsert_Factory::instance()->create( psAllocatedAmount,
													  psAllocationDate.c_str(),
													  psFullMaturity,
													  psCreditMethod.c_str(),
													  psLocked,
													  psImpactBatchOnly,
													  knetData.getUseTimeBand(),
													  knetData.getHasSchedule(),
													  knetData.getAutomaticAllocTransfer(),
													  knetData.getUseValueDateReview(),
													  knetData.getEconomicCapitalLimit(),
													  knetData.getLimitGroup(),
													  knetData.getIsEntity(),
													  psRefModeCpty.c_str(),
													  psRefModeIndustry.c_str(),
													  psRefModeCountry.c_str(),
													  psSovereignKind.c_str(),
													  psRefModeFolder.c_str(),
													  psRefModeCurrency.c_str(),
													  psRefModeKNUser.c_str(),
													  psRefModeInstrument.c_str(),
													  psRefModeProject.c_str(),
													  psLimitKind.c_str(),
													  knetData.getCapitalLimit(),
													  status,
													  psCurrency );



	// next, fill in non mandatory fields
	KNETToCovPS( handle, knetData,
				 std_static_cast( RELATED_PS_COV_CLASS_VAR )( object ), false );

	// attache to this root its associated sub object
	insertReviewDate( object, knetData, handle );
	// A priorie pas besoin de mettre a jour la last et nextReviewDate
	// puisque ces deux champs sont read only :)
	//	updateLastAndNextReviewDateFields( object, knetData, handle );

	insertAllocationSchedule( object, knetData, handle );


	insertTBCoverageElt( object, knetData, handle );
	// De meme pour les credit limit associes aux AllocationSchedules
	// pas la peine de les creer elle ne seront pas utilisee dans le cas present
	// (I.E. DV insert process )
	KH_DBG::dbg("KNCB_CreditLimit::createInsertProcessFromKNET::method_end");
	return object;
}


KNCB_CreditLimit::RELATED_PS_CLASS_VAR
KNCB_CreditLimit::createFromDVCoverage( KNET_RequestHandle       handle,
                                        RELATED_PS_COV_CLASS_VAR base )
{

	KH_DBG::dbg("KNCB_CreditLimit::createFromDVCoverage::method_start");
  RELATED_KNET_CLASS_ACCESS access;

  // store data from database into an access KNETData
  PSToKNET( base, access );

  // create a change KNETData with it
  RELATED_KNET_CLASS_CHANGE change( access );

  // then create a new record with this change KNETData
  RELATED_PS_CLASS_VAR object = createFromKNET( handle, change, &*(base->Id()) );

  // attache to this record its sub elements
  insertReviewDate( object, change, handle );
  updateLastAndNextReviewDateFields( object, change, handle );
  insertAllocationSchedule( object, change, handle );
  insertTBCoverageElt( object, change, handle );
  insertCreditLimitElements( object, change, handle );

  //	createDefaultAccessRecords( handle->getUser(), object );
  KH_DBG::dbg("KNCB_CreditLimit::createFromDVCoverage::method_end");
  return object;
}


string KNCB_CreditLimit::getLimitCoverageIdSQLColumnName()
{
  return string("CreditLimitCoverageId");
}


string KNCB_CreditLimit::getAccessClass_ClassIdSQLColumnName()
{
  return string("DataId");
}


bool KNCB_CreditLimit::isLimitKindConcerned()
{
  return true;
}


void KNCB_CreditLimit::psQueryAccessibleLimits(char  const* cptyRefMode,
    PS_Oid_var const& cptyId,
    char  const* folderRefMode,
    PS_Oid_var const& folderId,
    char  const* countryRefMode,
    PS_Oid_var const& countryId,
    char  const* industryRefMode,
    PS_Oid_var const& industryId,
    char  const* instrumentRefMode,
    PS_Oid_var const& instrumentId,
    char  const* currencyRefMode,
    PS_Oid_var const& currencyId,
    char  const* userRefMode,
    PS_Oid_var const& userId,
    PS_Oid_var const& limitCoverageId,
	PS_Oid_var const& riskWeightCoverageId,
	char  const* projectRefMode,
    PS_Oid_var const& projectCoverageId,
    PS_Oid_var const& timeBandId,
    PS_Oid_var const& ratingAgencyId,
    PS_Oid_var const& ratingId,
    bool * capitalLimit,
    bool * economicCapitalLimit,
    PS_String_var const& limitKind,
    PS_String_var const& status,
    PS_Oid_var  const &RequestUser,
    PS_Time_var const &RequestDateUpperBound,
    PS_Time_var const &RequestDateLowerBound,
    PS_Oid_var  const &ValidationUser,
    PS_Time_var const &ValidationDateUpperBound,
    PS_Time_var const &ValidationDateLowerBound,
    int maxLenght,
    PS_Oid_var const& userAccessId,
    CreditLimitMaster_Factory::CLMasterDVCoverage_Coll_var& coll)
{
  coll = KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->queryLimits(cptyRefMode
         ,cptyId
         ,folderRefMode
         ,folderId
         ,countryRefMode
         ,countryId
         ,industryRefMode
         ,industryId
         ,instrumentRefMode
         ,instrumentId
         ,currencyRefMode
         ,currencyId
         ,userRefMode
         ,userId
         ,limitCoverageId
         ,riskWeightCoverageId
		 ,projectRefMode
         ,projectCoverageId
         ,timeBandId
         ,ratingAgencyId
         ,ratingId
         ,capitalLimit
         ,economicCapitalLimit
         ,&limitKind
         ,&status
         ,RequestUser
         ,RequestDateUpperBound
         ,RequestDateLowerBound
         ,ValidationUser
         ,ValidationDateUpperBound
         ,ValidationDateLowerBound
         ,maxLenght
         ,userAccessId);
}


void KNCB_CreditLimit::psQueryAccessibleLimits( bool  cptyRefMode,
    PS_Oid_var const& cptyId,
    bool folderRefMode,
    PS_Oid_var const& folderId,
    bool countryRefMode,
    PS_Oid_var const& countryId,
    bool industryRefMode,
    PS_Oid_var const& industryId,
    bool instrumentRefMode,
    PS_Oid_var const& instrumentId,
    bool currencyRefMode,
    PS_Oid_var const& currencyId,
    bool userRefMode,
    PS_Oid_var const& userId,
    PS_Oid_var const& limitCoverageId,
    bool limitCoverageNULL,
    PS_Oid_var const& riskWeightCoverageId,
    bool riskWeightCoverageNULL,
	//bool projectRefMode,
    PS_Oid_var const& projectCoverageId,
    bool projectCoverageNULL,
    PS_Oid_var const& timeBandId,
    bool ratingAgencyRefMode,
    PS_Oid_var const& ratingAgencyId,
    bool ratingRefMode,
    PS_Oid_var const& ratingId,
    bool * capitalLimit,
    bool * economicCapitalLimit,
    PS_String_var const& limitKind,
    PS_String_var const& status,
    PS_Oid_var  const &RequestUser,
    PS_Time_var const &RequestDateUpperBound,
    PS_Time_var const &RequestDateLowerBound,
    PS_Oid_var  const &ValidationUser,
    PS_Time_var const &ValidationDateUpperBound,
    PS_Time_var const &ValidationDateLowerBound,
    int maxLenght,
    PS_Oid_var const& userAccessId,
    CreditLimitMaster_Factory::CLMasterDVCoverage_Coll_var& coll)
{
  coll = KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->
         queryLimits(cptyRefMode
                     ,cptyId
                     ,folderRefMode
                     ,folderId
                     ,countryRefMode
                     ,countryId
                     ,industryRefMode
                     ,industryId
                     ,instrumentRefMode
                     ,instrumentId
                     ,currencyRefMode
                     ,currencyId
                     ,userRefMode
                     ,userId
                     ,limitCoverageId
                     ,limitCoverageNULL
                     ,riskWeightCoverageId
                     ,riskWeightCoverageNULL
                     //,projectRefMode
                     ,projectCoverageId
                     ,projectCoverageNULL
                     ,timeBandId
                     ,ratingAgencyRefMode
                     ,ratingAgencyId
                     ,ratingRefMode
                     ,ratingId
                     ,capitalLimit
                     ,economicCapitalLimit
                     ,&limitKind
                     ,&status
                     ,RequestUser
                     ,RequestDateUpperBound
                     ,RequestDateLowerBound
                     ,ValidationUser
                     ,ValidationDateUpperBound
                     ,ValidationDateLowerBound
                     ,maxLenght
                     ,userAccessId);
}


CreditReservation_var
KNCB_CreditLimit::createCreditReservationFromKNET( KNET_RequestHandle handle
    ,CreditLimit_var const& arcCreditLimit
    ,KNET_CreditReservationChange const& knetCreditReservation )
{
  char status[2] = { KNDBC_Choices::VALIDATION_STATUS_ENABLE, 0};


  CreditReservation_var object;
  //reservation attachee a la creditlimit ou a la creditlimitmaster
  object
  = CreditReservation_Factory::instance()->create(
      knetCreditReservation.getAllocatedAmount() // double AllocatedAmount
      ,KNETToPSRefModeIG(knetCreditReservation.getCptyRefMode()).c_str() // const char* RefMode_Cpty
      ,KNETToPSRefMode(knetCreditReservation.getCountryRefMode()).c_str() // const char* RefMode_Country
      ,KNETToPSRefMode(knetCreditReservation.getIndustryRefMode()).c_str() // const char* RefMode_Industry
      ,KNETToPSRefMode(knetCreditReservation.getFolderRefMode()).c_str() // const char* RefMode_Folder
      ,KNETToPSRefMode(knetCreditReservation.getCurrencyRefMode()).c_str() // const char* RefMode_Currency
      ,KNETToPSRefMode(knetCreditReservation.getUserRefMode()).c_str() // const char* RefMode_KNUser
      ,KNETToPSRefMode(knetCreditReservation.getInstrumentRefMode()).c_str() // const char* RefMode_Instrument
      , status
      ,0 // double UsedAmount
      ,arcCreditLimit // KNCB_CreditLimit::RELATED_PS_CLASS_VAR arcCreditLimit
    );



  KNETToPSCreditReservation(handle, arcCreditLimit, knetCreditReservation, object, false);
  return object;
}
/*
 * KNETToPSCreditReservation
 */
void
KNCB_CreditLimit::KNETToPSCreditReservation(KNET_RequestHandle handle
    ,CreditLimit_var const& arcCreditLimit
    ,KNET_CreditReservationChange const& knetCreditReservation
    ,CreditReservation_var& object
    ,bool setMandatoryAttributes)
{

  /*=============================
    Mandatory attributes
    =============================*/
  if (setMandatoryAttributes)
    {
      /*
       * CreditLimitId
       */
      /*object->arcCreditLimit(KNCBTK_CoreBasic<KNCB_CreditLimit::RELATED_PS_CLASS_VAR
        ,KNCB_CreditLimit::RELATED_PS_FACTORY>
        ::queryId(creditLimitId);*/

      object->arcCreditLimit(arcCreditLimit);

      /*
       * RefMode_Cpty
       */
      object->RefMode_Cpty(KNETToPSRefModeIG(knetCreditReservation.getCptyRefMode()).c_str());
      /*
       * RefMode_Country
       */
      object->RefMode_Country(KNETToPSRefMode(knetCreditReservation.getCountryRefMode()).c_str());
      /*
       * RefMode_Industry
       */
      object->RefMode_Industry(KNETToPSRefMode(knetCreditReservation.getIndustryRefMode()).c_str());
      /*
       * RefMode_Folder
       */
      object->RefMode_Folder(KNETToPSRefMode(knetCreditReservation.getFolderRefMode()).c_str());
      /*
       * RefMode_Currency
       */
      object->RefMode_Currency(KNETToPSRefMode(knetCreditReservation.getCurrencyRefMode()).c_str());
      /*
       * RefMode_KNUser
       */
      object->RefMode_KNUser(KNETToPSRefMode(knetCreditReservation.getUserRefMode()).c_str());
      /*
       * RefMode_Instrument
       */
      object->RefMode_Instrument(KNETToPSRefMode(knetCreditReservation.getInstrumentRefMode()).c_str());
      /*
       * AllocatedAmount
       */
      object->AllocatedAmount(knetCreditReservation.getAllocatedAmount());
      /*
       * UsedAmount
       */
      //object->UsedAmount(knetCreditReservation.getUsedAmount());
    }
  /*=============================
    NULL allowed attributes
    =============================*/
  /*
   * CptyCoverage (NULL allowed)
   */
  if (knetCreditReservation.isCptyCoverageNULL())
    object->arcCpty(Cpty_var());///////////////////////set to NULL??????
  else
    {
      KGR_Id knetId;
      if	(!KNCBTK_Identifier<CptyAlias_var
          ,CptyAlias_Factory>
          ::KNET_IdentifierToId(&knetCreditReservation.getCptyCoverage()
                                ,handle->getSource()
                                ,knetId)
         )
        {
          ;
        }
      object->arcCpty(KNCBTK_CoreBasic<Cpty_var
                      ,Cpty_Factory>
                      ::queryId(knetId));
    }
  /*
   * CountryCoverage (NULL allowed)
   */
  if (knetCreditReservation.isCountryCoverageNULL())
    object->arcCountry(Country_var());///////////////////////set to NULL??????
  else
    {
      KGR_Id knetId;
      if	(!KNCBTK_Identifier<CountryAlias_var
          ,CountryAlias_Factory>
          ::KNET_IdentifierToId(&knetCreditReservation.getCountryCoverage()
                                ,handle->getSource()
                                ,knetId)
         )
        {
          ;
        }
      object->arcCountry(KNCBTK_CoreBasic<Country_var
                         ,Country_Factory>
                         ::queryId(knetId));
    }
  /*
   * IndustryCoverage (NULL allowed)
   */
  if (knetCreditReservation.isIndustryCoverageNULL())
    object->arcIndustry(Industry_var());///////////////////////set to NULL??????
  else
    {
      KGR_Id knetId;
      if	(!KNCBTK_Identifier<IndustryAlias_var
          ,IndustryAlias_Factory>
          ::KNET_IdentifierToId(&knetCreditReservation.getIndustryCoverage()
                                ,handle->getSource()
                                ,knetId)
         )
        {
          ;
        }
      object->arcIndustry(KNCBTK_CoreBasic<Industry_var
                          ,Industry_Factory>
                          ::queryId(knetId));
    }
  /*
   * FolderCoverage (NULL allowed)
   */
  if (knetCreditReservation.isFolderCoverageNULL())
    object->arcFolder(Folder_var());///////////////////////set to NULL??????
  else
    {
      KGR_Id knetId;
      if	(!KNCBTK_Identifier<FolderAlias_var
          ,FolderAlias_Factory>
          ::KNET_IdentifierToId(&knetCreditReservation.getFolderCoverage()
                                ,handle->getSource()
                                ,knetId)
         )
        {
          ;
        }
      object->arcFolder(KNCBTK_CoreBasic<Folder_var
                        ,Folder_Factory>
                        ::queryId(knetId));
    }
  /*
   * RatingCoverage (NULL allowed)
   */
  if (knetCreditReservation.isRatingCoverageNULL())
    object->arcRating(Rating_var());///////////////////////set to NULL??????
  else
    {
      KGR_Id knetId;
      if	(!KNCBTK_Identifier<RatingAlias_var
          ,RatingAlias_Factory>
          ::KNET_IdentifierToId(&knetCreditReservation.getRatingCoverage()
                                ,handle->getSource()
                                ,knetId)
         )
        {
          ;
        }
      object->arcRating(KNCBTK_CoreBasic<Rating_var
                        ,Rating_Factory>
                        ::queryId(knetId));
    }
  /*
   * RatingAgencyCoverage (NULL allowed)
   */
  if (knetCreditReservation.isRatingAgencyCoverageNULL())
    object->arcRatingAgency(RatingAgency_var());///////////////////////set to NULL??????
  else
    {
      KGR_Id knetId;
      if	(!KNCBTK_Identifier<RatingAgencyAlias_var
          ,RatingAgencyAlias_Factory>
          ::KNET_IdentifierToId(&knetCreditReservation.getRatingAgencyCoverage()
                                ,handle->getSource()
                                ,knetId)
         )
        {
          ;
        }
      object->arcRatingAgency(KNCBTK_CoreBasic<RatingAgency_var
                              ,RatingAgency_Factory>
                              ::queryId(knetId));
    }
  /*
   * CurrencyCoverage (NULL allowed)
   */
  if (knetCreditReservation.isCurrencyCoverageNULL())
    object->arcCurrency(Currency_var());///////////////////////set to NULL??????
  else
    {
      KGR_Id knetId;
      if	(!KNCBTK_Identifier<CurrencyAlias_var
          ,CurrencyAlias_Factory>
          ::KNET_IdentifierToId(&knetCreditReservation.getCurrencyCoverage()
                                ,handle->getSource()
                                ,knetId)
         )
        {
          ;
        }
      object->arcCurrency(KNCBTK_CoreBasic<Currency_var
                          ,Currency_Factory>
                          ::queryId(knetId));
    }
  /*
   * KNUserCoverage (NULL allowed)
   */
  if (knetCreditReservation.isUserCoverageNULL())
    object->arcKNUser(KNUser_var());///////////////////////set to NULL??????
  else
    {
      KGR_Id knetId;
      if	(!KNCBTK_Identifier<KNUserAlias_var
          ,KNUserAlias_Factory>
          ::KNET_IdentifierToId(&knetCreditReservation.getUserCoverage()
                                ,handle->getSource()
                                ,knetId)
         )
        {
          ;
        }
      KNUser_var psUser = KNCBTK_CoreBasic<KNUser_var
                          ,KNUser_Factory>
                          ::queryId(knetId);
      TODO("enum");
      if (psUser->Purpose().buff()[0]=='A')
        {
          throw_LOGICAL(" User Coverage should have User Identification as Purpose");
        }

      object->arcKNUser(psUser);
    }
  /*
  * InstrumentCoverage (NULL allowed)
  */
  if (knetCreditReservation.isInstrumentCoverageNULL())
    object->arcInstrument(Instrument_var());///////////////////////set to NULL??????
  else
    {
      KGR_Id knetId;
      if	(!KNCBTK_Identifier<InstrumentAlias_var
          ,InstrumentAlias_Factory>
          ::KNET_IdentifierToId(&knetCreditReservation.getInstrumentCoverage()
                                ,handle->getSource()
                                ,knetId)
         )
        {
          ;
        }
      object->arcInstrument(KNCBTK_CoreBasic<Instrument_var
                            ,Instrument_Factory>
                            ::queryId(knetId));
    }
  /*
  * TimeBandCoverage (NULL allowed)
  */


  /*
   * BeginDate (NULL allowed)
  */
  if (knetCreditReservation.isBeginDateNULL())
    object->BeginDateNULL(true);
  else
    object->BeginDate(KNET_DateToPS(knetCreditReservation.getBeginDate()).c_str());
  /*
  * EndDate (NULL allowed)
  */
  if (knetCreditReservation.isEndDateNULL())
    object->EndDateNULL(true);
  else
    object->EndDate(KNET_DateToPS(knetCreditReservation.getEndDate()).c_str());
  /*
  * KNUserId_Approval (NULL allowed)
  */
  if (knetCreditReservation.isUserApprovalNULL())
    object->arcValidationApvlUser(KNUser_var());///////////////////////set to NULL??????
  else
    {
      KGR_Id knetId;
      if	(!KNCBTK_Identifier<KNUserAlias_var
          ,KNUserAlias_Factory>
          ::KNET_IdentifierToId(&knetCreditReservation.getUserApproval()
                                ,handle->getSource()
                                ,knetId)
         )
        {
          ;
        }
      KNUser_var psUserApproval = KNCBTK_CoreBasic<KNUser_var
                                  ,KNUser_Factory>
                                  ::queryId(knetId);
      //		TODO("enum");
      if (psUserApproval->Purpose().buff()[0]=='A')
        {
          throw_LOGICAL(" User Approval should have User Identification as Purpose");
        }
      object->arcValidationApvlUser(psUserApproval);
    }
  /*
  * Annotation (NULL allowed)
  */
  if (knetCreditReservation.isAnnotationNULL())
    object->AnnotationNULL(true);
  else
    object->Annotation(knetCreditReservation.getAnnotation());
  /*
  * CreditLimitId_Transfer (NULL allowed)
  */

  object->arcCreditLimitTransfer(CreditLimit_var());////////////////////////set to NULL??????

  /*
  * CreditReservationId_Transfer (NULL allowed)
  */
  object->arcCreditReservationTransfer1(CreditReservation_var());
  ;///////////////////////set to NULL??????
}
/*
* PSToKNETCreditReservation
*/
void
KNCB_CreditLimit::PSToKNETCreditReservation(CreditReservation_var const& object
    ,KNET_CreditReservationAccess& knetCreditReservation)
{
	/*=============================
	  Mandatory attributes
	  =============================*/
	/*****
	 * Id
	 *****/
	knetCreditReservation.setId(KGR_Id(object->Id()->getOidVal()));
	/*
	 * CreditLimitId
	 */

	CreditLimit_var psCL
		= CreditLimit_Factory::instance()->queryKey(*object->CreditLimitId()
													,PS_Defs::k_cacheThenDatabase);


	if(!PS_is_nil(psCL))
	{
		knetCreditReservation.setCreditLimit(KGR_Id(psCL->CreditLimitMasterId()->getOidVal()));

		CreditLimitMaster_var psCreditLimitMaster
			= CreditLimitMaster_Factory::instance()->queryKey(*psCL->CreditLimitMasterId()
															  ,PS_Defs::k_cacheThenDatabase);
		knetCreditReservation.setCreditLimitIdentity(KNCBTK_IdentityTool<CreditLimitMaster_var,
													 CreditLimitMaster_Factory,
													 CreditLimitMaster_Iter_var,
													 CreditLimitMaster_Cltn_var>
													 ::getIdentity(psCreditLimitMaster,
																   psCreditLimitMaster->Id()));
	}
	/*
	 * RefMode_Cpty
	 */
	knetCreditReservation.setCptyRefMode(PSToKNETRefModeIG(object->RefMode_Cpty()));
	/*
	 * RefMode_Country
	 */
	knetCreditReservation.setCountryRefMode(PSToKNETRefMode(object->RefMode_Country()));
	/*
	 * RefMode_Industry
	 */
	knetCreditReservation.setIndustryRefMode(PSToKNETRefMode(object->RefMode_Industry()));
	/*
	 * RefMode_Folder
	 */
	knetCreditReservation.setFolderRefMode(PSToKNETRefMode(object->RefMode_Folder()));
	/*
	 * RefMode_Currency
	 */
	knetCreditReservation.setCurrencyRefMode(PSToKNETRefMode(object->RefMode_Currency()));
	/*
	 * RefMode_KNUser
	 */
	knetCreditReservation.setUserRefMode(PSToKNETRefMode(object->RefMode_KNUser()));
	/*
	 * RefMode_Instrument
	 */
	knetCreditReservation.setInstrumentRefMode(PSToKNETRefMode(object->RefMode_Instrument()));
	/*
	 * AllocatedAmount
	 */
	knetCreditReservation.setAllocatedAmount(object->AllocatedAmount());
	/*
	 * UsedAmount
	 */
	knetCreditReservation.setUsedAmount(object->UsedAmount());
	/*=============================
	  NULL allowed attributes
	  =============================*/
	/*
	 * CptyCoverage (NULL allowed)
	 */
	if (object->CptyId_CoverageNULL())
    {
		knetCreditReservation.setCptyCoverageNULL();
    }
	else
    {
		Cpty_var psCptyCoverage
			= Cpty_Factory::instance()->queryKey(*object->CptyId_Coverage()
												 ,PS_Defs::k_cacheThenDatabase);
		knetCreditReservation.setCptyCoverage(KNCBTK_IdentityTool<Cpty_var,
											  Cpty_Factory,
											  Cpty_Iter_var,
											  Cpty_Cltn_var>
											  ::getIdentity(psCptyCoverage, object->CptyId_Coverage()));
    }
	/*
	 * CountryCoverage (NULL allowed)
	 */
	if (object->CountryId_CoverageNULL())
    {
		knetCreditReservation.setCountryCoverageNULL();
    }
	else
    {
		Country_var psCountryCoverage
			= Country_Factory::instance()->queryKey(*object->CountryId_Coverage()
													,PS_Defs::k_cacheThenDatabase);
		knetCreditReservation.setCountryCoverage(KNCBTK_IdentityTool<Country_var,
												 Country_Factory,
												 Country_Iter_var,
												 Country_Cltn_var>
												 ::getIdentity(psCountryCoverage, object->CountryId_Coverage()));
    }
	/*
	 * IndustryCoverage (NULL allowed)
	 */
	if (object->IndustryId_CoverageNULL())
    {
		knetCreditReservation.setIndustryCoverageNULL();
    }
	else
    {
		Industry_var psIndustryCoverage
			= Industry_Factory::instance()->queryKey(*object->IndustryId_Coverage()
													 ,PS_Defs::k_cacheThenDatabase);
		knetCreditReservation.setIndustryCoverage(KNCBTK_IdentityTool<Industry_var,
												  Industry_Factory,
												  Industry_Iter_var,
												  Industry_Cltn_var>
												  ::getIdentity(psIndustryCoverage, object->IndustryId_Coverage()));
    }
	/*
	 * FolderCoverage (NULL allowed)
	 */
	if (object->FolderId_CoverageNULL())
    {
		knetCreditReservation.setFolderCoverageNULL();
    }
	else
    {
		Folder_var psFolderCoverage
			= Folder_Factory::instance()->queryKey(*object->FolderId_Coverage()
												   ,PS_Defs::k_cacheThenDatabase);
		knetCreditReservation.setFolderCoverage(KNCBTK_IdentityTool<Folder_var,
												Folder_Factory,
												Folder_Iter_var,
												Folder_Cltn_var>
												::getIdentity(psFolderCoverage, object->FolderId_Coverage()));
    }
	/*
	 * RatingCoverage (NULL allowed)
	 */
	if (object->RatingId_CoverageNULL())
    {
		knetCreditReservation.setRatingCoverageNULL();
    }
	else
    {
		Rating_var psRatingCoverage
			= Rating_Factory::instance()->queryKey(*object->RatingId_Coverage()
												   ,PS_Defs::k_cacheThenDatabase);
		knetCreditReservation.setRatingCoverage(KNCBTK_IdentityTool<Rating_var,
												Rating_Factory,
												Rating_Iter_var,
												Rating_Cltn_var>
												::getIdentity(psRatingCoverage, object->RatingId_Coverage()));
    }
	/*
	 * RatingAgencyCoverage (NULL allowed)
	 */
	if (object->RatingAgencyIdNULL())
    {
		knetCreditReservation.setRatingAgencyCoverageNULL();
    }
	else
    {
		RatingAgency_var psRatingAgencyCoverage
			= RatingAgency_Factory::instance()->queryKey(*object->RatingAgencyId()
														 ,PS_Defs::k_cacheThenDatabase);
		knetCreditReservation.setRatingAgencyCoverage(KNCBTK_IdentityTool<RatingAgency_var,
													  RatingAgency_Factory,
													  RatingAgency_Iter_var,
													  RatingAgency_Cltn_var>
													  ::getIdentity(psRatingAgencyCoverage, object->RatingAgencyId()));
    }
	/*
	 * CurrencyCoverage (NULL allowed)
	 */
	if (object->CurrencyId_CoverageNULL())
    {
		knetCreditReservation.setCurrencyCoverageNULL();
    }
	else
    {
		Currency_var psCurrencyCoverage
			= Currency_Factory::instance()->queryKey(*object->CurrencyId_Coverage()
													 ,PS_Defs::k_cacheThenDatabase);
		knetCreditReservation.setCurrencyCoverage(KNCBTK_IdentityTool<Currency_var,
												  Currency_Factory,
												  Currency_Iter_var,
												  Currency_Cltn_var>
												  ::getIdentity(psCurrencyCoverage, object->CurrencyId_Coverage()));
    }
	/*
	 * KNUserCoverage (NULL allowed)
	 */
	if (object->KNUserId_CoverageNULL())
    {
		knetCreditReservation.setUserCoverageNULL();
    }
	else
    {
		KNUser_var psKNUserCoverage
			= KNUser_Factory::instance()->queryKey(*object->KNUserId_Coverage()
												   ,PS_Defs::k_cacheThenDatabase);
		knetCreditReservation.setUserCoverage(KNCBTK_IdentityTool<KNUser_var,
											  KNUser_Factory,
											  KNUser_Iter_var,
											  KNUser_Cltn_var>
											  ::getIdentity(psKNUserCoverage, object->KNUserId_Coverage()));
    }
	/*
	 * InstrumentCoverage (NULL allowed)
	 */
	if (object->InstrumentId_CoverageNULL())
    {
		knetCreditReservation.setInstrumentCoverageNULL();
    }
	else
    {
		Instrument_var psInstrumentCoverage
			= Instrument_Factory::instance()->queryKey(*object->InstrumentId_Coverage()
													   ,PS_Defs::k_cacheThenDatabase);
		knetCreditReservation.setInstrumentCoverage(KNCBTK_IdentityTool<Instrument_var,
													Instrument_Factory,
													Instrument_Iter_var,
													Instrument_Cltn_var>
													::getIdentity(psInstrumentCoverage, object->InstrumentId_Coverage()));
    }
	/*
	 * TimeBandCoverage (NULL allowed)
	 */
	TODO("decommenter les lignes suivantes lorsque le champs TimeBandId_Coverage sera ajoute a la table CreditReservation");
	/*if (object->TimeBandId_CoverageNULL())
	  {
	  knetCreditReservation.setTimeBandCoverageNULL();
	  }
	  else
	  {
	  TimeBand_var psTimeBandCoverage
	  = TimeBand_Factory::instance()->queryKey(*object->TimeBandId_Coverage()
	  ,PS_Defs::k_cacheThenDatabase);
	  knetCreditReservation.setTimeBandCoverage(KNCBTK_IdentityTool<TimeBand_var,
	  TimeBand_Factory,
	  TimeBand_Iter_var,
	  TimeBand_Cltn_var>
	  ::getIdentity(psTimeBandCoverage, object->TimeBandId_Coverage()));
	  }*/
	/*
	 * BeginDate (NULL allowed)
	 */
	if (object->BeginDateNULL())
		knetCreditReservation.setBeginDateNULL();
	else
		knetCreditReservation.setBeginDate(PSToKGR_Date(object->BeginDate()));
	/*
	 * EndDate (NULL allowed)
	 */
	if (object->EndDateNULL())
		knetCreditReservation.setEndDateNULL();
	else
		knetCreditReservation.setEndDate(PSToKGR_Date(object->EndDate()));
	/*
	 * KNUserId_Approval (NULL allowed)
	 */
	if (object->ApprovingUserIdNULL())
    {
		knetCreditReservation.setUserApprovalNULL();
    }
	else
    {
		KNUser_var psKNUserApproval
			= KNUser_Factory::instance()->queryKey(*object->ApprovingUserId()
												   ,PS_Defs::k_cacheThenDatabase);
		knetCreditReservation.setUserApproval(KNCBTK_IdentityTool<KNUser_var,
											  KNUser_Factory,
											  KNUser_Iter_var,
											  KNUser_Cltn_var>
											  ::getIdentity(psKNUserApproval, object->ApprovingUserId()));
    }
	/*
	 * Annotation (NULL allowed)
	 */
	if (object->AnnotationNULL())
		knetCreditReservation.setAnnotationNULL();
	else
		knetCreditReservation.setAnnotation(object->Annotation());
	/*
	 * CreditLimitId_Transfer (NULL allowed)
	 */
	/*
	 * CreditReservationId_Transfer (NULL allowed)
	 */
}

/*
* createCreditReservationTransferFromKNET
* ???CREATE???
*/
void
KNCB_CreditLimit::createCreditReservationTransferFromKNET(KNET_RequestHandle handle
    ,CreditLimit_var const& creditLimitSource
    ,CreditLimit_var const& creditLimitDestination
    ,KNET_CreditReservationTransferChange const& knetCreditReservationTransfer
    ,CreditReservation_var& creditReservationTransferSource
    ,CreditReservation_var& creditReservationTransferDestination)
{
  char status[2] = { KNDBC_Choices::VALIDATION_STATUS_ENABLE, 0};


  CreditLimitMaster_var psCreditLimitMasterSource = CreditLimitMaster_Factory::instance()->queryKey(*creditLimitSource->CreditLimitMasterId(),PS_Defs::k_cacheThenDatabase) ;
  CreditLimitMaster_var psCreditLimitMasterDestination = CreditLimitMaster_Factory::instance()->queryKey(*creditLimitDestination->CreditLimitMasterId(),PS_Defs::k_cacheThenDatabase) ;

  if (PS_is_nil(psCreditLimitMasterSource) || PS_is_nil(psCreditLimitMasterDestination))
    {
      KNDB_T_ROLLBACK
      string errMsg(CreditLimit_Factory::instance()->className());
      errMsg+=" destination not found";
      KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
      return;
    }

  double rate = KNCB_CreditLimit_getRate(psCreditLimitMasterSource,
                                         psCreditLimitMasterDestination);
  double psAllocatedAmountSource= rate*knetCreditReservationTransfer.getAllocatedAmount();
  double psAllocatedAmountDestination=(-1)*knetCreditReservationTransfer.getAllocatedAmount();
  //



  creditReservationTransferSource
  = CreditReservation_Factory::instance()->create(
      psAllocatedAmountSource // double AllocatedAmount
      ,KNETToPSRefMode(KNET_Limit::REF_MODE_ANY).c_str() // const char* RefMode_Cpty
      ,KNETToPSRefMode(KNET_Limit::REF_MODE_ANY).c_str() // const char* RefMode_Country
      ,KNETToPSRefMode(KNET_Limit::REF_MODE_ANY).c_str() // const char* RefMode_Industry
      ,KNETToPSRefMode(KNET_Limit::REF_MODE_ANY).c_str() // const char* RefMode_Folder
      ,KNETToPSRefMode(KNET_Limit::REF_MODE_ANY).c_str() // const char* RefMode_Currency
      ,KNETToPSRefMode(KNET_Limit::REF_MODE_ANY).c_str() // const char* RefMode_KNUser
      ,KNETToPSRefMode(KNET_Limit::REF_MODE_ANY).c_str() // const char* RefMode_Instrument
      ,status
      ,0 // double UsedAmount
      ,creditLimitSource // KNCB_CreditLimit::RELATED_PS_CLASS_VAR arcCreditLimit
    );
  creditReservationTransferDestination
  = CreditReservation_Factory::instance()->create(
      psAllocatedAmountDestination // double AllocatedAmount
      ,KNETToPSRefMode(KNET_Limit::REF_MODE_ANY).c_str() // const char* RefMode_Cpty
      ,KNETToPSRefMode(KNET_Limit::REF_MODE_ANY).c_str() // const char* RefMode_Country
      ,KNETToPSRefMode(KNET_Limit::REF_MODE_ANY).c_str() // const char* RefMode_Industry
      ,KNETToPSRefMode(KNET_Limit::REF_MODE_ANY).c_str() // const char* RefMode_Folder
      ,KNETToPSRefMode(KNET_Limit::REF_MODE_ANY).c_str() // const char* RefMode_Currency
      ,KNETToPSRefMode(KNET_Limit::REF_MODE_ANY).c_str() // const char* RefMode_KNUser
      ,KNETToPSRefMode(KNET_Limit::REF_MODE_ANY).c_str() // const char* RefMode_Instrument
      ,status
      ,0 // double UsedAmount
      ,creditLimitDestination // KNCB_CreditLimit::RELATED_PS_CLASS_VAR arcCreditLimit
    );


  KNETToPSCreditReservationTransfer(handle
                                    ,creditLimitSource
                                    ,creditLimitDestination
                                    ,knetCreditReservationTransfer
                                    ,creditReservationTransferSource
                                    ,creditReservationTransferDestination
                                    ,false);
}
/*
 * KNETToPSCreditReservationTransfer
 */
void
KNCB_CreditLimit::KNETToPSCreditReservationTransfer(KNET_RequestHandle handle
    ,CreditLimit_var const& creditLimitSource
    ,CreditLimit_var const& creditLimitDestination
    ,KNET_CreditReservationTransferChange const& knetCreditReservationTransfer
    ,CreditReservation_var& creditReservationTransferSource
    ,CreditReservation_var& creditReservationTransferDestination
    ,bool setMandatoryAttributes
                                                   )
{
  static const char*fctName = "KNCB_CreditLimit::KNETToPSCreditReservationTransfer";

  CreditLimitMaster_var psCreditLimitMasterSource = CreditLimitMaster_Factory::instance()->queryKey(*creditLimitSource->CreditLimitMasterId(),PS_Defs::k_cacheThenDatabase) ;
  CreditLimitMaster_var psCreditLimitMasterDestination = CreditLimitMaster_Factory::instance()->queryKey(*creditLimitDestination->CreditLimitMasterId(),PS_Defs::k_cacheThenDatabase) ;

  if (PS_is_nil(psCreditLimitMasterSource) || PS_is_nil(psCreditLimitMasterDestination))
    {
      KNDB_T_ROLLBACK
      string errMsg(CreditLimit_Factory::instance()->className());
      errMsg+=" destination not found";
      KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND, errMsg.c_str(), handle);
      return;
    }

  double rate = KNCB_CreditLimit_getRate(psCreditLimitMasterSource,
                                         psCreditLimitMasterDestination);

  /*====================================
   * !! Set TWO CreditReservation_var !!
   *===================================*/
  CreditReservation_var object;
  double psAllocatedAmount;
  CreditLimit_var creditLimit;
  CreditLimit_var creditLimitTransfer;

  CreditReservation_var creditReservationTransfer;
  int i=0;
  for(;i<2;++i)
    {
      if (i==0)
        {
          object=creditReservationTransferSource;
          creditLimit=creditLimitSource;
          psAllocatedAmount=rate*knetCreditReservationTransfer.getAllocatedAmount();
          creditLimitTransfer=creditLimitDestination;
          creditReservationTransfer=creditReservationTransferDestination;
        }
      else
        {
          object=creditReservationTransferDestination;
          creditLimit=creditLimitDestination;
          psAllocatedAmount=-knetCreditReservationTransfer.getAllocatedAmount();
          creditLimitTransfer=creditLimitSource;
          creditReservationTransfer=creditReservationTransferSource;
        }

      /*=============================
      			Mandatory attributes
      =============================*/
      if (setMandatoryAttributes)
        {
          /*
          * CreditLimitId
          */

          object->arcCreditLimit(creditLimit);

          /*
          * AllocatedAmount
          */
          object->AllocatedAmount(psAllocatedAmount);
        }
      /*=============================
      		NULL allowed attributes
      =============================*/
      /*
      * BeginDate (NULL allowed)
      */
      if (knetCreditReservationTransfer.isBeginDateNULL())
        object->BeginDateNULL(true);
      else
        object->BeginDate(KNET_DateToPS(knetCreditReservationTransfer.getBeginDate()).c_str());
      /*
      * EndDate (NULL allowed)
      */
      if (knetCreditReservationTransfer.isEndDateNULL())
        object->EndDateNULL(true);
      else
        object->EndDate(KNET_DateToPS(knetCreditReservationTransfer.getEndDate()).c_str());
      /*
      * KNUserId_Approval (NULL allowed)
      */
      if (knetCreditReservationTransfer.isUserApprovalNULL())
        object->arcValidationApvlUser(KNUser_var());///////////////////set to NULL??????
      else
        {
          KGR_Id knetId;
          if	(!KNCBTK_Identifier<KNUserAlias_var
              ,KNUserAlias_Factory>
              ::KNET_IdentifierToId(&knetCreditReservationTransfer.getUserApproval()
                                    ,handle->getSource()
                                    ,knetId)
             )
            {
              ;
            }
          KNUser_var psUserApproval = KNCBTK_CoreBasic<KNUser_var
                                      ,KNUser_Factory>
                                      ::queryId(knetId);
          //			TODO("enum");
          if (psUserApproval->Purpose().buff()[0]=='A')
            {
              throw_LOGICAL(" User Approval should have User Identification as Purpose");
            }

          object->arcValidationApvlUser(psUserApproval);
        }
      /*
      * Annotation (NULL allowed)
      */
      if (knetCreditReservationTransfer.isAnnotationNULL())
        object->AnnotationNULL(true);
      else
        object->Annotation(knetCreditReservationTransfer.getAnnotation());
      /*========================================================================================*/
      /*
      * CreditLimitId_Transfer (NULL allowed)
      */

      object->arcCreditLimitTransfer(creditLimitTransfer);

      /*
      * CreditReservationId_Transfer (NULL allowed)
      */
      object->arcCreditReservationTransfer1(creditReservationTransfer);
    }
}
/*
* PSToKNETCreditReservationTransfer
*/
void
KNCB_CreditLimit::PSToKNETCreditReservationTransfer(CreditReservation_var const& object
    ,KNET_CreditReservationTransferAccess& knetCreditReservationTransfer)
{

  /*=============================
  			Mandatory attributes
  =============================*/
  /*****
  * Id
  *****/
  knetCreditReservationTransfer.setId(KGR_Id(object->Id()->getOidVal()));
  /*
  * CreditLimitId
  */

  CreditLimit_var CLVar =CreditLimit_Factory::instance()->queryKey(*object->CreditLimitId()
                         ,PS_Defs::k_cacheThenDatabase);

  if(!PS_is_nil(CLVar))
    {
      //the CL key is a masterId and a timeBandId
      knetCreditReservationTransfer.setSourceLimitId(KGR_Id(CLVar->CreditLimitMasterId()->getOidVal()));
      knetCreditReservationTransfer.setSourceTimeBandId(KGR_Id(CLVar->TimeBandId()->getOidVal()));
    }
  /*
  * AllocatedAmount
  */
  knetCreditReservationTransfer.setAllocatedAmount(object->AllocatedAmount());
  //TRACE_LOG << object->AllocatedAmount() << endl ;
  /*=============================
  		NULL allowed attributes
  =============================*/
  /*
  * BeginDate (NULL allowed)
  */
  if (object->BeginDateNULL())
    knetCreditReservationTransfer.setBeginDateNULL();
  else
    knetCreditReservationTransfer.setBeginDate(PSToKGR_Date(object->BeginDate()));
  /*
  * EndDate (NULL allowed)
  */
  if (object->EndDateNULL())
    knetCreditReservationTransfer.setEndDateNULL();
  else
    knetCreditReservationTransfer.setEndDate(PSToKGR_Date(object->EndDate()));
  /*
  * KNUserId_Approval (NULL allowed)
  */
  if (object->ApprovingUserIdNULL())
    {
      knetCreditReservationTransfer.setUserApprovalNULL();
    }
  else
    {
      KNUser_var psKNUserApproval
      = KNUser_Factory::instance()->queryKey(*object->ApprovingUserId()
                                             ,PS_Defs::k_cacheThenDatabase);
      knetCreditReservationTransfer.setUserApproval(KNCBTK_IdentityTool<KNUser_var,
          KNUser_Factory,
          KNUser_Iter_var,
          KNUser_Cltn_var>
          ::getIdentity(psKNUserApproval, object->ApprovingUserIdNULL()));
    }
  /*
  * Annotation (NULL allowed)
  */
  if (object->AnnotationNULL())
    knetCreditReservationTransfer.setAnnotationNULL();
  else
    knetCreditReservationTransfer.setAnnotation(object->Annotation());
  /*
  * CreditLimitId_Transfer (NULL allowed) // but never NULL in this case (for a transfer)
  */
  //thus, the CL key is a masterId and a timeBandId
  CreditLimit_var CLDestVar = CreditLimit_Factory::instance()->queryKey(*object->CreditLimitId_Transfer()
																		,PS_Defs::k_cacheThenDatabase);

  if(!PS_is_nil(CLDestVar))
  {
	  knetCreditReservationTransfer.setDestinationLimitId(KGR_Id(CLDestVar->CreditLimitMasterId()->getOidVal()));
	  knetCreditReservationTransfer.setDestinationTimeBandId(KGR_Id(CLDestVar->TimeBandId()->getOidVal()));
  }

  /*
  * CreditReservationId_Transfer (NULL allowed)
  */
}
/*
* PSToKNETNetting
*/
KNET_DealHeaderChange::Netting
KNCB_CreditLimit::PSToKNETNetting(PS_String_var const& psNetting)
{
  if (!strcmp(psNetting,"N"))
    return KNET_DealHeaderChange::KNET_NORMAL;
  else if (!strcmp(psNetting,"E"))
    return KNET_DealHeaderChange::KNET_FORCE; //ENFORCE
  else if (!strcmp(psNetting,"P"))
    return KNET_DealHeaderChange::KNET_FORBID; //PREVENT
  assert(!"KNCB_CreditLimit::PSToKNETNetting mismatch");
  return KNET_DealHeaderChange::KNET_NORMAL;
}

/*
* PSToKNETCreditDeal
*/
void
KNCB_CreditLimit::PSToKNETCreditDeal(DealLog_var const& psDealLog
                                     ,CreditLog_var const& psCreditLog
                                     ,KNET_CreditDeal& knetCreditDeal)
{
  /*!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  KNET_CreditDeal n'est pas calqu???e sur une table de la DB comme le sont les
  autres KNET_Data.
  KNET_CreditDeal regroupe une partie des donn???es extraites de deux (+1) tables :
  - DealLog et CreditLog
  - DealTableAlias
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!*/
  /*=============================
  			Mandatory attributes
  =============================*/
  /*****
  * KNET_Deal: Id
  * (DealLog) Id
  *****/
  knetCreditDeal.setId(KGR_Id(psDealLog->Id()->getOidVal()));
  /*
  * KNET_Deal: Source
  * (DealLog) SourceId
  */
  Source_var psSource
  = Source_Factory::instance()->queryKey(*psDealLog->SourceId()
                                         ,PS_Defs::k_cacheThenDatabase);
  knetCreditDeal.setSource(KNCBTK_IdentityTool<Source_var
                           ,Source_Factory
                           ,Source_Iter_var
                           ,Source_Cltn_var>
                           ::getIdentity(psSource, psDealLog->SourceId()));
  /*
  * KNET_Deal: DealTable
  * (DealLog) DealTableId
  */
  DealTable_var psDealTable
  = DealTable_Factory::instance()->queryKey(*psDealLog->DealTableId()
      ,PS_Defs::k_cacheThenDatabase);
  knetCreditDeal.setDealTable(KNCBTK_IdentityTool<DealTable_var
                              ,DealTable_Factory
                              ,DealTable_Iter_var
                              ,DealTable_Cltn_var>
                              ::getIdentity(psDealTable, psDealLog->DealTableId()));
  /*
  * KNET_Deal: DealStamp
  * (DealLog) DealStamp
  */
  knetCreditDeal.setDealStamp(psDealLog->DealStamp());
  /*
  * KNET_Deal: User
  * (DealLog) KNUserId
  */
  KNUser_var psKNUser
  = KNUser_Factory::instance()->queryKey(*psDealLog->KNUserId()
                                         ,PS_Defs::k_cacheThenDatabase);
  knetCreditDeal.setUser(KNCBTK_IdentityTool<KNUser_var
                         ,KNUser_Factory
                         ,KNUser_Iter_var
                         ,KNUser_Cltn_var>
                         ::getIdentity(psKNUser, psDealLog->KNUserId()));
  /*
  * KNET_Deal: Cpty
  * (CreditLog) CptyId
  */
  Cpty_var psCpty
  = Cpty_Factory::instance()->queryKey(*psCreditLog->CptyId()
                                       ,PS_Defs::k_cacheThenDatabase);
  knetCreditDeal.setCpty(KNCBTK_IdentityTool<Cpty_var
                         ,Cpty_Factory
                         ,Cpty_Iter_var
                         ,Cpty_Cltn_var>
                         ::getIdentity(psCpty, psCreditLog->CptyId()));
  /*
  * KNET_Deal: Folder
  * (CreditLog) FolderId
  */
  Folder_var psFolder
  = Folder_Factory::instance()->queryKey(*psCreditLog->FolderId()
                                         ,PS_Defs::k_cacheThenDatabase);
  knetCreditDeal.setFolder(KNCBTK_IdentityTool<Folder_var
                           ,Folder_Factory
                           ,Folder_Iter_var
                           ,Folder_Cltn_var>
                           ::getIdentity(psFolder, psCreditLog->FolderId()));
  /*
  * KNET_Deal: Instrument
  * (CreditLog) InstrumentId
  */
  Instrument_var psInstrument
  = Instrument_Factory::instance()->queryKey(*psCreditLog->InstrumentId()
      ,PS_Defs::k_cacheThenDatabase);
  knetCreditDeal.setInstrument(KNCBTK_IdentityTool<Instrument_var
                               ,Instrument_Factory
                               ,Instrument_Iter_var
                               ,Instrument_Cltn_var>
                               ::getIdentity(psInstrument, psCreditLog->InstrumentId()));
  /*
  * KNET_Deal: Currency
  * (CreditLog) CurrencyId
  */
  Currency_var psCurrency
  = Currency_Factory::instance()->queryKey(*psCreditLog->CurrencyId()
      ,PS_Defs::k_cacheThenDatabase);
  knetCreditDeal.setCurrency(KNCBTK_IdentityTool<Currency_var
                             ,Currency_Factory
                             ,Currency_Iter_var
                             ,Currency_Cltn_var>
                             ::getIdentity(psCurrency, psCreditLog->CurrencyId()));
  /*
  * KNET_Deal: Active
  * (DealLog) Active
  */
  knetCreditDeal.setActive(psDealLog->Active());
  /*
  * KNET_Deal: NoRisks
  * (DealLog) NoRisk
  */
  knetCreditDeal.setNoRisks(PSToKNETNoRisk(psDealLog->NoRisk()));
  /*
  * KNET_Deal: OneOffs
  * (DealLog) OneOff
  */
  knetCreditDeal.setOneOffs(PSToKNETNoRisk(psDealLog->OneOff()));
  /*
  * KNET_Deal: Netting
  * (DealLog) Netting
  */
  knetCreditDeal.setNetting(PSToKNETNetting(psDealLog->Netting()));
  /*
  * KNET_Deal: Exposure
  * (CreditLog) Exposure
  */
  knetCreditDeal.setExposure(psCreditLog->Exposure());
  /*
  * KNET_Deal: Matching
  * (CreditLog) Matching
  */
  knetCreditDeal.setMatching(psCreditLog->Exposure());
  /*
  * KNET_Deal: CaptureDate
  * (DealLog) CaptureDate
  */
  knetCreditDeal.setCaptureDate(PSTotime_t(psDealLog->CaptureDate()));
  /*
  * KNET_Deal: HasDoneTrial
  * (DealLog) HasDoneTrial
  */
  knetCreditDeal.setHasDoneTrial(PSToKNETHasDoneTrial(psDealLog->HasDoneTrial()));
  /*
  * KNET_Deal: HasDoneEnquiry
  * (DealLog) HasDoneEnquiry
  */
  knetCreditDeal.setHasDoneEnquiry(psDealLog->HasDoneEnquiry());
  /*
  * KNET_CreditDeal: TradeDate
  * (CreditLog) TradeDate
  */
  knetCreditDeal.setTradeDate(PSTotime_t(psCreditLog->TradeDate()));
  /*
  * KNET_CreditDeal: Direction
  * (CreditLog) Direction
  */
  knetCreditDeal.setDirection(psCreditLog->Direction());
  /*
  * KNET_CreditDeal: NominalValue
  * (CreditLog) NominalValue
  */
  knetCreditDeal.setNominalValue(psCreditLog->NominalValue());
  /*
  * KNET_CreditDeal: MarketValue
  * (CreditLog) MarketValue
  */
  knetCreditDeal.setMarketValue(psCreditLog->MarketValue());
  /*
  * KNET_CreditDeal: Sensitivity
  * (CreditLog) Sensitivity
  */
  knetCreditDeal.setSensitivity(psCreditLog->Sensitivity());
  /*
  * KNET_CreditDeal: GuaranteeType
  * (CreditLog) GuaranteeType
  */
  knetCreditDeal.setGuaranteeTypes(PSToKNETGuaranteeType(psCreditLog->GuaranteeType()));
  /*
  * KNET_CreditDeal: GuaranteePercent //REMOVED
  * (CreditLog) GuaranteePercent
  */
  ////knetCreditDeal.setGuaranteePercent(psCreditLog->GuaranteePercent());
  /*
  * KNET_CreditDeal: LegNumber
  * (CreditLog) CreditLeg
  */
  knetCreditDeal.setLegNumber(psCreditLog->CreditLeg());
  /*
  * KNET_CreditDeal: CreditKind
  * (CreditLog) CreditKind
  */
  knetCreditDeal.setCreditKind(PSToKNETCreditKind(psCreditLog->CreditKind()));
  /*
  * KNET_CreditDeal: FixedNoDays
  * (CreditLog) FixedNoDay
  */
  knetCreditDeal.setFixedNoDays(psCreditLog->FixedNoDay());

  knetCreditDeal.setGuaranteeMode(
    KNDBC_ConvChoice::Ps2KNET_GuaranteeMode( *psCreditLog->GuaranteeMode().buff() ) );

  /*=============================
  		NULL allowed attributes
  =============================*/
  /*
  * KNET_Deal: DealTableAlias (NULL allowed)
  */
  DealTableAlias_Cltn_var cltn = psDealTable->arcDealTableAliases();
  if (cltn->length()>0)
    {
      

      KGR_Alias* knetAlias = new KGR_Alias(cltn[(unsigned long) 0.0]->ObjectAlias());
      knetCreditDeal.setDealTableAlias(knetAlias);
      delete knetAlias;
      // Oui...de fa???on g???n???rale, on consid???re qu'il n'y a au plus qu'un seul alias par
      // objet (et pour une source donn???e) alors que la DB permet d'en avoir plusieurs...
    }
  else
    knetCreditDeal.setDealTableAliasNULL();
  /*
  * KNET_CreditDeal: ValueDate (NULL allowed)
  * (CreditLog) ValueDate
  */
  knetCreditDeal.setValueDate(PSTotime_t(psCreditLog->ValueDate()));
  /*
  * KNET_CreditDeal: MaturityDate (NULL allowed)
  * (CreditLog) MaturityDate
  */
  knetCreditDeal.setMaturityDate(PSToKGR_Date(psCreditLog->MaturityDate()));// PSTotime_t(psCreditLog->MaturityDate())
  /*
  * KNET_CreditDeal: IssueDate (NULL allowed)
  * (CreditLog) IssueDate
  */
  knetCreditDeal.setIssueDate(PSTotime_t(psCreditLog->IssueDate()));
  /*
  * KNET_CreditDeal: SettlementDate (NULL allowed)
  * (CreditLog) SettlementDate
  */
  knetCreditDeal.setSettlementDate(PSTotime_t(psCreditLog->SettlementDate()));
  /*
  * KNET_CreditDeal: OptionDate (NULL allowed)
  * (CreditLog) OptionDate
  */
  knetCreditDeal.setOptionDate(PSToKGR_Date(psCreditLog->OptionDate()));
  /*
  * KNET_CreditDeal: ExcessCode (NULL allowed)
  * (DealLog) ExcessCode (NULL allowed)
  */
  if (psDealLog->ExcessCodeNULL())
    knetCreditDeal.setExcessCodeNULL();
  else
    knetCreditDeal.setExcessCode(psDealLog->ExcessCode());
  /*
  * KNET_CreditDeal: CptyIssuer (NULL allowed)
  * (CreditLog) CptyId_Issuer
  */
  if (psCreditLog->CptyId_IssuerNULL())
    knetCreditDeal.setCptyIssuerNULL();
  else
    knetCreditDeal.setCptyIssuer(KNCBTK_IdentityTool<Cpty_var
                                 ,Cpty_Factory
                                 ,Cpty_Iter_var
                                 ,Cpty_Cltn_var>
                                 ::getIdentity(psCreditLog->arcIssuerCpty()
                                               ,psCreditLog->CptyId_Issuer()
                                              )
                                );

  /*
  * KNET_CreditDeal: GuaranteePercentCpty (NULL allowed)
  * (CreditLog) GuaranteePercent_Cpty
  */
  if (psCreditLog->GuaranteePercent_CptyNULL())
    knetCreditDeal.setGuaranteeValueCptyNULL();
  else
    knetCreditDeal.setGuaranteeValueCpty(psCreditLog->GuaranteePercent_Cpty());
  /*
  * KNET_CreditDeal: GuaranteePercentCountry (NULL allowed)
  * (CreditLog) GuaranteePercent_Country
  */
  if (psCreditLog->GuaranteePercent_CountryNULL())
    knetCreditDeal.setGuaranteeValueCountryNULL();
  else
    knetCreditDeal.setGuaranteeValueCountry(psCreditLog->GuaranteePercent_Country());
  /*
  * KNET_CreditDeal: GuaranteeLeg (NULL allowed)
  * (CreditLog) GuaranteeLeg
  */
  if (psCreditLog->GuaranteeLegNULL())
    knetCreditDeal.setGuaranteeLegNULL();
  else
    knetCreditDeal.setGuaranteeLeg(psCreditLog->GuaranteeLeg());
  /*
  * KNET_CreditDeal: CollateralizedLeg (NULL allowed)
  * (CreditLog) CollateralizedLeg
  */
  if (psCreditLog->CollateralLegNULL())
    knetCreditDeal.setCollateralizedLegNULL();
  else
    knetCreditDeal.setCollateralizedLeg(psCreditLog->CollateralLeg());

}


KNET_DoubleValidation::ValidableData KNCB_CreditLimit::getValidableDataType()
{
  return KNET_DoubleValidation::VALIDABLE_DATA_CREDIT_LIMIT;
}


KNDBC_Choices::VALIDATION_KIND
KNCB_CreditLimit::getValidationKind( ValidationSetup_var const &setup ) const
  {
    switch( *setup->OnCreditLimit().buff() )
      {
      case 'N' :
      case 'I' :
      case 'E' :
        return ( KNDBC_Choices::VALIDATION_KIND ) *setup->OnCreditLimit().buff();
      default:
        assert( !"The column OnCreditLimit from the ValidationSetup table contain an unexpected value" );
        return KNDBC_Choices::VALIDATION_KIND_NONE;
      }
  }


/*===================================================================================
  AllocationSchedule
===================================================================================*/


void
KNCB_CreditLimit::insertAllocationSchedule(
	CreditLimitMasterBase_var        creditLimitMaster,
    RELATED_KNET_CLASS_CHANGE const &data,
    KNET_RequestHandle               handle )
{
  KH_DBG::dbg("KNCB_CreditLimit::insertAllocationSchedule::method_start");
  hasTableAccessOrThrow( INS,
                         CreditAllocSchedElt_Factory::instance()->className(),
                         handle->getUser() );

  KGR_Collection<KGL_AllocationSchedule> const &allocationScheduleColl =
    data.getAllocationSchedule();

  int size = allocationScheduleColl.size();

  for( int idx = 0; idx < size; ++idx )
  {
      CreditAllocSchedElt_Factory_var factory =
        CreditAllocSchedElt_Factory::instance();

      CreditAllocSchedElt_var object =
        factory->create( allocationScheduleColl[ idx ].getAllocation(),
                         creditLimitMaster );

      object->BeginDate( KNET_DateToPS( allocationScheduleColl[ idx ].getBeginDate() ).c_str() );

      object->EndDate( KNET_DateToPS( allocationScheduleColl[ idx ].getEndDate() ).c_str() );


  }
  KH_DBG::dbg("KNCB_CreditLimit::insertAllocationSchedule::method_end");

}


void KNCB_CreditLimit::removeAllocationSchedule( CreditLimitMasterBase_var creditLimitMaster, //dataId is a CreditLimitId or TimeBandCoverageElementId
    KNET_RequestHandle        handle )
{
	KH_DBG::dbg("KNCB_CreditLimit::removeAllocationSchedule::start");
  hasTableAccessOrThrow( DEL,
                         CreditAllocSchedElt_Factory::instance()->className(),
                         handle->getUser() );

  KGLDB_WhereClause whereClause;
  whereClause.addCondition("CreditLimitMasterId", "=", creditLimitMaster->Id() );

  CreditAllocSchedElt_Cltn_var collToRemove =
    CreditAllocSchedElt_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());

  unsigned long idx = 0;

  for( ; idx < collToRemove->length(); ++idx )
    CreditAllocSchedElt_Factory::instance()->remove
    ( collToRemove[(unsigned long) idx] );

  KH_DBG::dbg("KNCB_CreditLimit::removeAllocationSchedule::end");

}


void
KNCB_CreditLimit::updateAllocationSchedule( CreditLimitMasterBase_var        creditLimitMaster,			//dataId is a CreditLimitId or TimeBandCoverageElementId
    RELATED_KNET_CLASS_CHANGE const &data,
    KNET_RequestHandle               handle )
{
  KH_DBG::dbg("KNCB_CreditLimit::updateAllocationSchedule::method_start");
  removeAllocationSchedule( creditLimitMaster, handle );
  insertAllocationSchedule( creditLimitMaster, data, handle );
  KH_DBG::dbg("KNCB_CreditLimit::updateAllocationSchedule::method_end");
}


void
updateOverdraftMode(double allocatedAmount, double usedAmount,
					CreditLimit_var cl)
{
	char newOverdraftMode[2], oldOverdraftMode[2];
	newOverdraftMode[0] = oldOverdraftMode[0] = *cl->OverdraftMode().buff();
	newOverdraftMode[1] = oldOverdraftMode[1] = 0;
	
	if ((allocatedAmount-usedAmount)>=0)
		*newOverdraftMode = KNDBC_Choices::OVERDRAFT_MODE_NONE;
	else
		*newOverdraftMode = KNDBC_Choices::OVERDRAFT_MODE_BATCH;

	//should we keep old OverdraftMode	value ?
	switch(*oldOverdraftMode)
	{
		case KNDBC_Choices::OVERDRAFT_MODE_LOCK:
		case KNDBC_Choices::OVERDRAFT_MODE_LOCKED:
		case KNDBC_Choices::OVERDRAFT_MODE_TIME:
// 		case KNDBC_Choices::OVERDRAFT_MODE_RESERVATION_EXCESS:
// 		case KNDBC_Choices::OVERDRAFT_MODE_SMALL_EXCESS:
// 		case KNDBC_Choices::OVERDRAFT_MODE_ALMOST_EXCEEDED:
// 		case KNDBC_Choices::OVERDRAFT_MODE_DEAL:
// 		case KNDBC_Choices::OVERDRAFT_MODE_NONE:
// 		case KNDBC_Choices::OVERDRAFT_MODE_UNDER_USED:
// 		case KNDBC_Choices::OVERDRAFT_MODE_VALIDATION:
			*newOverdraftMode = *oldOverdraftMode;
			break;

		default:
		break;
	}

		
	cl->OverdraftMode(newOverdraftMode);  
}

void KNCB_CreditLimit::insertCreditLimitElements( RELATED_PS_CLASS_VAR creditLimitMaster,
												  RELATED_KNET_CLASS_CHANGE const &data,
												  KNET_RequestHandle handle ){
	KGR_Collection< KGL_TimeBandCoverageElementChange > const &TBCoverageColl =
		data.getTimeBandCoverageElement();

	if( TBCoverageColl.size() == 0 )
    {
		// we are in the infinite timeband case => 0D-+
		TimeBand_var tb;
		KGLDB_WhereClause whereClause;
		whereClause.addCondition( "ShortName", "=", INFINIT_TB_SHORTNAME );
			
		if(!data.isLimitCoverageNULL())
		{
			//If we have a defaut Timeband in the Product Exposure we need to use it instead of 0d-+
			CreditLimitCoverage_var  limCovv=getVar<CreditLimitCoverage>( data.getLimitCoverage() );
			if (!limCovv->TimeBandIdNULL()  && actualMode_==INSERT_MODE)
			{
				tb = TimeBand_Factory::instance()->queryKey( *limCovv->TimeBandId(), PS_Defs::k_cacheThenDatabase  );
			}
			else
			{
				TimeBand_Cltn_var tbCltn = TimeBand_Factory::instance()->querySQLWhere( whereClause.getConditions().c_str() );
		         if(!PS_is_nil(tbCltn) &&
		                tbCltn->length())
		                tb = tbCltn[0ul];
			}
		}
		else
		{
			TimeBand_Cltn_var tbCltn = TimeBand_Factory::instance()->querySQLWhere( whereClause.getConditions().c_str() );
	         if(!PS_is_nil(tbCltn) &&
	                tbCltn->length())
	                tb = tbCltn[0ul];
		}



		CreditLimit_var psCreditLimit = createDefaultCreditLimit( *tb->Id(),
																  creditLimitMaster->LimitKind(),
																  creditLimitMaster );

		if(!PS_is_nil( psCreditLimit ))
		{
			psCreditLimit->AllocatedAmount(creditLimitMaster->AllocatedAmount());
		}
    }
	else
    {
		//delete de l'element tb infini ( celui avec TimeBandId=null dans notre cas provisoire 0D-999Y)

		/*
		  KGLDB_WhereClause whereClause;
		  whereClause.addCondition("CreditLimitMasterId", "=",KGR_Id(creditLimitMaster->Id()->getOidVal()));
		  whereClause.addIsNullCondition("TimeBandId");

		  TimeBandCoverageElt_Cltn_var collTB =
		  TimeBandCoverageElt_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());

		  if(collTB->length()!=0)
		  TimeBandCoverageElt_Factory::instance()->remove(collTB[(unsigned long) 0]);
		*/
    }

#ifdef DEBUG
	TRACE_LOG<<"KNCB_CreditLimit::insertCreditLimitElements"<<endl;
	TRACE_LOG<<"Management of External Risk Engine, Update Credit Limit with Time Bands"<<endl;
#endif

	for( unsigned long idx = 0; idx < TBCoverageColl.size(); ++idx ){
		TimeBand_var psTimeBand =
			getVar<TimeBand>( TBCoverageColl[ idx ].getTimeBand(),
							  handle->getSource() );

		// here generation of n limit according to the time band coverage defined

		CreditLimit_var psCreditLimit = createDefaultCreditLimit( *psTimeBand->Id(),
																  creditLimitMaster->LimitKind(),
																  creditLimitMaster );
		if(!PS_is_nil( psCreditLimit ))
		{
			psCreditLimit->AllocatedAmount( TBCoverageColl[ idx ].getAllocatedAmount() );
		}
    }
}

// BEGIN KLE EXTERNAL_RISK_ENGINE
void KNCB_CreditLimit::updateCreditLimitElements( RELATED_PS_CLASS_VAR creditLimitMaster,
												  RELATED_KNET_CLASS_CHANGE const &data,
												  KNET_RequestHandle handle ){

	KGR_Collection< KGL_TimeBandCoverageElementChange > const &TBCoverageColl =
		data.getTimeBandCoverageElement();

	CreditLimit_Cltn_var psCltnCreditLimit = creditLimitMaster->arcCreditLimits();
	bool useTimeBand = TBCoverageColl.size()>0;
	CreditLimit_var psCreditLimit;

	if(PS_is_nil(psCltnCreditLimit)) return;

	if( 0 == psCltnCreditLimit->length() ) return;

	psCreditLimit = psCltnCreditLimit[0ul];
	if(PS_is_nil(psCreditLimit)) return;

	if(!useTimeBand)
	{
		psCreditLimit->AllocatedAmount(data.getAllocatedAmount());
		// update overdraftMode because of change of AllocatedAmount
		// but this should not be done here, as it does not include consideration of all objects that participate to the computation of overdraftmode in real-time
			
		// having changed a limit, this is updating a deal in real-time
		// or launching a batch that guarantees the exact update of UsedAmount and OverdraftMode, and not a trigger of a data property change

		updateOverdraftMode(data.getAllocatedAmount(), psCreditLimit->UsedAmount(),
							psCreditLimit);
	}

	//while(useTimeBand && psCreditLimit)
	unsigned long idx = 0;
	for ( ; useTimeBand && idx < psCltnCreditLimit->length(); ++idx)
	{
#ifdef DEBUG
		TRACE_LOG<<"KNCB_CreditLimit::updateCreditLimitElements()"<<endl;
		TRACE_LOG<<"Management of External Risk Engine, Update Credit Limits"<<endl;
#endif

		psCreditLimit = psCltnCreditLimit[idx];

		int TBSize = TBCoverageColl.size(), idx;
 		for(idx = 0; idx < TBSize ; idx++){
 			const KGR_Identifier *pIdentifier = &TBCoverageColl[idx].getTimeBand();

			bool usedMCNetCollatWasModified = false;
			double oldUsedAmountMCNetCollat = 0.0;
 			if(pIdentifier->getType() == KGR_Identifier::ALIAS) continue;

			KGR_Id TBId(psCreditLimit->TimeBandId()->getOidVal());
			if(TBId !=  *(KGR_Id *)pIdentifier) continue;

			psCreditLimit->AllocatedAmount(TBCoverageColl[idx].getAllocatedAmount());

			// update overdraftMode because of change of AllocatedAmount
			// but this should not be done here, as it does not include consideration of all objects that participate to the computation of overdraftmode in real-time
				
			// having changed a limit, this is updating a deal in real-time
			// or launching a batch that guarantees the exact update of UsedAmount and OverdraftMode, and not a trigger of a data property change
	
			updateOverdraftMode(TBCoverageColl[idx].getAllocatedAmount(),
								psCreditLimit->UsedAmount(),
								psCreditLimit);

			// on vient de traiter le bon TBelement, on sort du for
			// pour passer a l'element suivant de psCltnCreditLimit
			break;
 		}

	}
}
// END KLE EXTERNAL_RISK_ENGINE

/*===================================================================================
  TimeBandCoverageElement
  ===================================================================================*/
void KNCB_CreditLimit::insertTBCoverageElt( CreditLimitMasterBase_var creditLimitMaster,
											RELATED_KNET_CLASS_CHANGE const &data,
											KNET_RequestHandle handle ){

	KH_DBG::dbg("insertTBCoverageElt::start");

	hasTableAccessOrThrow( INS,
						   TimeBandCoverageElt_Factory::instance()->className(),
						   handle->getUser() );

  KGR_Collection<KGL_TimeBandCoverageElementChange> const &TBCoverageColl =
    data.getTimeBandCoverageElement();

  for( unsigned long i = 0; i < TBCoverageColl.size(); ++i )
    {
      KGR_Id knetId;

      TimeBand_var psTimeBand =
        getVar<TimeBand>(TBCoverageColl[i].getTimeBand(),handle->getSource());

      TimeBandCoverageElt_Factory_var fact =
        TimeBandCoverageElt_Factory::instance();

      TimeBandCoverageElt_var object =
        fact->create( TBCoverageColl[i].getAllocatedAmount(), TBCoverageColl[i].getIsEligible(), creditLimitMaster,
                      psTimeBand );

      if (TBCoverageColl[i].isMessageNULL() )
        object->MsgNULL(true);
      else
        object->Msg(TBCoverageColl[i].getMessage() );


      //here for the allocation schedule by timeband.
      KGR_Collection<KGL_AllocationSchedule> const &allocationScheduleColl =
        TBCoverageColl[i].getAllocationSchedule() ;

      unsigned long j;
      for( j = 0; j < allocationScheduleColl.size(); ++j )
        {
          CreditTBAllocSchedElt_Factory_var fact =
            CreditTBAllocSchedElt_Factory::instance();

          CreditTBAllocSchedElt_var allocSchedule =
            fact->create( allocationScheduleColl[j].getAllocation(),
                          creditLimitMaster,
                          psTimeBand );

          allocSchedule->BeginDate( KNET_DateToPS( allocationScheduleColl[j].getBeginDate() ).c_str() );
          allocSchedule->EndDate( KNET_DateToPS( allocationScheduleColl[j].getEndDate() ).c_str() );
        }
    }
}


CreditLimit_var
KNCB_CreditLimit::createDefaultCreditLimit( PS_Oid const          &timeBand,
    PS_String_var          limitKind,
    CreditLimitMaster_var  creditLimitMaster )
{
  TODO( "un-hardwire enum here");
  return CreditLimit_Factory::instance()
         ->create( timeBand,
                   limitKind,
                   0,
				   0.0, // allocatedAmount
                   "N", // default overdraftMode
                   0, // NPVSum
                   0, // NPVSumA
                   0, // PosSum
                   0, // AddOnSum
                   0, // AddOnSumA
                   0.0, // AOSumAbsSum
                   0.0, // NPVNoNet
                   0.0, // NPVAddOnNoNet
                   0.0, // AddOnNoNet
                   0.0, // AddOnAbsNoNet
                   0.0, // UsedAmount_WoNet
                   0.0, // CollateralAmount
                   0.0, // CNASum
                   0.0, // NPVSum_WoNet
                   0.0, // NPVAddOnSum_WoNet
                   0.0, // AddOnSum_WoNet
                   0.0, // UsedAmount_MC
                   0.0, // UsedAmount_MCNet
                   0.0, // UsedAmount_MCNetCollat
                   0.0, // UsedAmountPL
                   0,   // NbUnderlyingNettingDeal
                   creditLimitMaster );
}

bool removeCreditLimit(const char * whereClause)
//, KNC_ServerParams serverParams )
{


	// whereClause should be returning a unique value, otherwise only the first one will be deleted.
	CreditLimit_Cltn_var clLogCltn = 
		CreditLimit_Factory::instance()->querySQLWhere(whereClause);
	if(!PS_is_nil(clLogCltn) && clLogCltn->length())
	{
		static const char* rowNumber = getenv( "ROWCOUNT_SIZE" );
		int rowNbParam = 0; //if 0, SP use 5000
		if(rowNumber && *rowNumber)
			rowNbParam = atoi(rowNumber);
		char rowNoBuffer[10];
		sprintf(rowNoBuffer, "%i", rowNbParam);
		
/* 		KNDB_Mutex aggrMutex(KNDB_Mutex::KNET_MUTEX_AGGREGATION, serverParams);
		while (!aggrMutex.EnterCS_Trans())
				sleep(1);
*/
		for (unsigned long i=0;i<clLogCltn->length();++i)
		{
			CreditLimit_var psCreditLimit = clLogCltn[i];
			string creditLimitIdStr = "0x" + KNC_ConvId::idToStr( (const char *)psCreditLimit->Id()->getOidVal());
			
			string condLog = "PurgeCreditLimitImpact NULL, ";
			condLog += creditLimitIdStr ;
			condLog += ", ";
			condLog += rowNoBuffer;;

			try {
#ifdef DEBUG
	TRACE_LOG<<"KNCB_CreditLimit::removeCreditLimit Remove CreditLimitElements="<<condLog<<endl;
#endif	
			CreditLimitMaster_Cltn_var clmLogCltn = CreditLimitMaster_Factory::instance()->querySP(condLog.c_str());
			}
			catch (const PS_UserError& e) {
#ifdef DEBUG
	ERROR_LOG<<"KNCB_CreditLimit::removeCreditLimit PS_UserError :"<<e.description()<<endl;
#endif	
			}
			catch (const PS_ServerError& e) {
#ifdef DEBUG
	ERROR_LOG<<"KNCB_CreditLimit::removeCreditLimit PS_ServerError :"<<e.description<<endl;
#endif	
			}
		}
		// remove the CreditLimit elements
		CreditLimit_Factory::instance()->removeObjectCltn(*clLogCltn);
/* 		while (!aggrMutex.LeaveCS_Trans())
			sleep(1);
*/

		return true;
	}

	return false;
}

void
KNCB_CreditLimit::updateTBCoverageElt( CreditLimitMaster_var            creditLimitMaster,
                                       RELATED_KNET_CLASS_CHANGE const &data,
                                       KNET_RequestHandle               handle )
{
	hasTableAccessOrThrow( UPD,
						   TimeBandCoverageElt_Factory::instance()->className(),
						   handle->getUser() );

	KGR_Collection<KGL_TimeBandCoverageElementChange> const &TBCoverageColl =
		data.getTimeBandCoverageElement();

	unsigned long idx=0;

	// create / udpate element of TimeBandCoverageElement
	for( ; idx < TBCoverageColl.size(); ++idx )
	{
		TimeBand_var psTimeBand =
			getVar<TimeBand>( TBCoverageColl[ idx ].getTimeBand(), handle->getSource() );

		if( !PS_is_nil( psTimeBand ) )
		{
			// try to fetch the old value if there are
			TimeBandCoverageElt_var object = TimeBandCoverageElt_Factory::instance()
				->queryKey( *creditLimitMaster->Id(),
							*psTimeBand->Id(), PS_Defs::k_cacheThenDatabase );
			// if we can't find any, we insert a new one
			if( PS_is_nil( object ) )
			{
				object = TimeBandCoverageElt_Factory::instance()
					->create( TBCoverageColl[ idx ].getAllocatedAmount(),
							  TBCoverageColl[ idx ].getIsEligible(),
							  creditLimitMaster,
							  psTimeBand );
				if (TBCoverageColl[ idx ].isMessageNULL() )
				{object->MsgNULL(true);}
				else
				{object->Msg(TBCoverageColl[ idx ].getMessage() );}

				// create (if exist) related timeband allocation schedule

				//here generation limit according to the time band coverage defined
				KGLDB_WhereClause whereClause1;
				whereClause1.addCondition( "CreditLimitMasterId", "=", creditLimitMaster->Id() );
				whereClause1.addCondition( "TimeBandId",          "=", psTimeBand->Id() );

				CreditLimit_Cltn_var Climit =
					CreditLimit_Factory::instance()->querySQLWhere( whereClause1.getConditions().c_str() );
				if( PS_is_nil(Climit) || 0 == Climit->length() )
				{
					CreditLimit_var clVar = createDefaultCreditLimit( *psTimeBand->Id(),
											creditLimitMaster->LimitKind(),
											creditLimitMaster );
					clVar->AllocatedAmount(TBCoverageColl[ idx ].getAllocatedAmount());
					// no setting of overdraftMode for this just created limit
				}
				else
				{
					CreditLimit_var clVar=Climit[0ul];
					clVar->AllocatedAmount(TBCoverageColl[ idx ].getAllocatedAmount());
					
					// update overdraftMode because of change of AllocatedAmount
					// but this should not be done here, as it does not include consideration of all objects that participate to the computation of overdraftmode in real-time
						
					// having changed a limit, this is updating a deal in real-time
					// or launching a batch that guarantees the exact update of UsedAmount and OverdraftMode, and not a trigger of a data property change
			
					updateOverdraftMode(TBCoverageColl[ idx ].getAllocatedAmount(),
										clVar->UsedAmount(),
										clVar);
				}
			}
			else // found, so update an existing timeband element
			{
				if (TBCoverageColl[ idx ].isMessageNULL() )
					{object->MsgNULL(true);}
				else
					{object->Msg(TBCoverageColl[ idx ].getMessage() );}
				object->IsTransferEligible( TBCoverageColl[ idx ].getIsEligible() );
				object->AllocatedAmount( TBCoverageColl[ idx ].getAllocatedAmount() );
			}
		} // end of psTimeBand ! = NILL
	} // end of for

	// Next, we have to check for the element which have been removed
	KGLDB_WhereClause whereClause;
	whereClause.addCondition( "CreditLimitMasterId", "=", creditLimitMaster->Id() );

	CreditLimit_Cltn_var collCLToRemove =
		CreditLimit_Factory::instance()->querySQLWhere( whereClause.getConditions().c_str() );

	TimeBand_var psInfiniteTimeBand = TimeBand_Factory::instance()->queryShortName( string(INFINIT_TB_SHORTNAME).c_str() );

	// update of a Credit Limit Master which had an INFINITE time band and keeps it
	if ( TBCoverageColl.size()==0
		&&  collCLToRemove->length()==1
		&& *collCLToRemove[0ul]->TimeBandId() == *psInfiniteTimeBand->Id())
	{
		CreditLimit_var cl = collCLToRemove[0ul];
		cl->AllocatedAmount(data.getAllocatedAmount());
		updateOverdraftMode(data.getAllocatedAmount(), cl->UsedAmount(),
							cl);
		// just update the CreditLimit No Delete
	}
	else {
		bool found = false;

		//when a limit if infinite (ie without time band), the TBColl is empty and de facto the time is 0D+-
		for( idx = 0; idx < collCLToRemove->length(); ++idx )
		{
			TimeBand_var psTimeBand1 =
				getVar<TimeBand>( collCLToRemove[(unsigned long) idx ]->TimeBandId() );

			found = false;
			// look into TimeBandCoverage Element of DV Limit and check the difference
			for( unsigned long k = 0; !found && k < TBCoverageColl.size(); ++k )
			{
				TimeBand_var psTimeBand2 =
					getVar<TimeBand>( TBCoverageColl[ k ].getTimeBand(),
									  handle->getSource() );

				found = (*psTimeBand1->Id() == *psTimeBand2->Id());
			}
			// if not found it means that the key (timebandId,limitmasterId) is in
			// database but not any more in data collection ==> it has been deleted

			// delete Credit Limit AND Time band coverage element if it does not exist in the new one
			if(  found == false)
			{
				whereClause.erase();
				whereClause.addCondition( "CreditLimitMasterId", "=", creditLimitMaster->Id() );
				whereClause.addCondition( "TimeBandId",          "=", psTimeBand1->Id() );
				

				// call to a stored procedure is faster than removal using PowerTier which deletes one by one.
				removeCreditLimit(whereClause.getConditions().c_str());
				removeSQLWhere< TimeBandCoverageElt > (whereClause.getConditions());
			}
			// else the Time band exists in DV and in master nothing to do
		}
		// next  insert CreditTBAllocSchedElt
		for( unsigned long k = 0; k < TBCoverageColl.size(); k++ )
		{
			TimeBand_var psTimeBand = getVar<TimeBand>( TBCoverageColl[k].getTimeBand(),
														handle->getSource() );

			if( PS_is_nil( psTimeBand ) )
				throw_NOTFOUND( KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->className() );

			// bug 8604
			KGLDB_WhereClause wClause;
			wClause.addCondition( "CreditLimitMasterId", "=", creditLimitMaster->Id() );
			wClause.addCondition( "TimeBandId", "=", psTimeBand->Id() );
			// remove allocation schedule linked to a TBCoverageElt
			removeSQLWhere<CreditTBAllocSchedElt>( wClause.getConditions() );
			// end 8604

			KGR_Collection< KGL_AllocationSchedule > const &allocationScheduleColl =
				TBCoverageColl[ k ].getAllocationSchedule();

			//insert collection of allocation schedule by time band
			for(  unsigned long idx = 0; idx < allocationScheduleColl.size(); ++idx )
			{
				CreditTBAllocSchedElt_Factory_var fact = CreditTBAllocSchedElt_Factory::instance();

				CreditTBAllocSchedElt_var object =
					fact->create( allocationScheduleColl[ idx ].getAllocation(),
								  creditLimitMaster,
								  psTimeBand );

				object->BeginDate( KNET_DateToPS( allocationScheduleColl[ idx ].getBeginDate() ).c_str() );
				object->EndDate(   KNET_DateToPS( allocationScheduleColl[ idx ].getEndDate() ).c_str() );
			}
		} // end for

		if ( 0 == TBCoverageColl.size() )
		{
			// If there is no more TB, we need to crate at least the CreditLimit for TB ]0-D+]
			CreditLimit_var psCreditLimit = createDefaultCreditLimit( *psInfiniteTimeBand->Id(),
																	  creditLimitMaster->LimitKind(),
																	  creditLimitMaster );
			psCreditLimit->AllocatedAmount(data.getAllocatedAmount());
		}
	}
}


void
KNCB_CreditLimit::removeTBCoverageElt( CreditLimitMasterBase_var creditLimitMaster,
                                       KNET_RequestHandle        handle )
{
  hasTableAccessOrThrow( DEL,
                         TimeBandCoverageElt_Factory::instance()->className(),
                         handle->getUser() );

  // build the common SQL reauest where clause
  KGLDB_WhereClause wClause;
  wClause.addCondition( "CreditLimitMasterId", "=", creditLimitMaster->Id() );

  // remove all timeband coverage and allocation schedule and Credit Limits
  // linked to a Credit Limit Master
  removeSQLWhere<CreditTBAllocSchedElt>( wClause.getConditions() );
  removeSQLWhere<TimeBandCoverageElt>  ( wClause.getConditions() );
  //removeCreditLimit(wClause.getConditions().c_str());
}


/*===================================================================================
  ReviewDate
  ===================================================================================*/


void
KNCB_CreditLimit::updateLastAndNextReviewDateFields( RELATED_PS_CLASS_VAR            creditLimitMaster,
    RELATED_KNET_CLASS_CHANGE const &data,
    KNET_RequestHandle               handle )
{
  KGR_Collection<KGL_ReviewDate> const &reviewDateColl = data.getReviewDates();

  KNC_Date today( KNC_ConvDate::getNow() );

  if( reviewDateColl.size() == 0 )
    creditLimitMaster->NextReviewDateNULL( true );
  else
    {

      //update of NextReviewDate :

	  unsigned long       idx = 0;
      bool      haveDateInTheFutur = false;
      KGR_Date date;
      KNC_Date  kncdate;
      KNC_Date  closestFromToday = today;

      for( idx = 0; idx < reviewDateColl.size(); ++idx )
        {
          kncdate =
            KNC_Date( reviewDateColl[ idx ].getReviewDate().getDay(),
                      reviewDateColl[ idx ].getReviewDate().getMonth(),
                      reviewDateColl[ idx ].getReviewDate().getYear(),
                      reviewDateColl[ idx ].getReviewDate().getHour(),
                      reviewDateColl[ idx ].getReviewDate().getMinute(),
                      reviewDateColl[ idx ].getReviewDate().getSecond() );

          if( date1less2( today, kncdate ) )
            {
              haveDateInTheFutur = true;
              date.setDate( kncdate );
              //TRACE_LOG << KNET_DateToPS( date ).c_str() << endl;

              // if we find a closer date from today distinct from today
              if( date1equal2( closestFromToday, today ) ||
                  date1less2( kncdate, closestFromToday ) )
                closestFromToday = kncdate;
            }
        }

      // if they are review dates in the futur, there is a new nextReviewDate
      if( haveDateInTheFutur )
        {
          KGR_Date converted;
          converted.setDate( closestFromToday );
          creditLimitMaster->NextReviewDate( KNET_DateToPS( converted ).c_str() );
        }
      else
        creditLimitMaster->NextReviewDateNULL( true );
    }

    // correction of bug 7103 - update of last review date
    // the last review date is set to today
    KGR_Date todayconverted;
    todayconverted.setDate( today );
    creditLimitMaster->LastReviewDate( KNET_DateToPS( todayconverted ).c_str());

}


void
KNCB_CreditLimit::insertReviewDate( CreditLimitMasterBase_var        creditLimitMaster,
                                    RELATED_KNET_CLASS_CHANGE const &data,
                                    KNET_RequestHandle               handle )
{
  hasTableAccessOrThrow( INS, ReviewCredElt_Factory::instance()->className(),
                         handle->getUser() );

  KGR_Collection<KGL_ReviewDate> const &reviewDateColl = data.getReviewDates();
  unsigned long idx = 0;

  for( ; idx < reviewDateColl.size(); ++idx )
    {
      ReviewCredElt_Factory_var factory = ReviewCredElt_Factory::instance();

      ReviewCredElt_var object =
        factory->create( KNET_DateToPS( reviewDateColl[ idx ].getReviewDate() ).c_str(),
                         creditLimitMaster );

      object->Msg( reviewDateColl[ idx ].getMessage() );

      if( !reviewDateColl[ idx ].isCommentNULL() )
        object->Annotation( reviewDateColl[ idx ].getComment() );
    }
}


void KNCB_CreditLimit::removeReviewDate( CreditLimitMasterBase_var creditLimitMaster,
    KNET_RequestHandle        handle )
{
  hasTableAccessOrThrow( DEL, ReviewCredElt_Factory::instance()->className(),
                         handle->getUser() );

  KGLDB_WhereClause whereClause;
  whereClause.addCondition( "CreditLimitMasterId", "=", creditLimitMaster->Id() );

  ReviewCredElt_Cltn_var collToRemove =
    ReviewCredElt_Factory::instance()->querySQLWhere( whereClause.getConditions().c_str() );

  unsigned long idx;
  for( idx = 0; idx < collToRemove->length(); ++idx )
    ReviewCredElt_Factory::instance()->remove
    ( collToRemove[ (unsigned long) idx ] );
}


void KNCB_CreditLimit::updateReviewDate( CreditLimitMaster_var            creditLimitMaster,
    RELATED_KNET_CLASS_CHANGE const &data,
    KNET_RequestHandle               hdl )
{
  // update = remove all + insert
  removeReviewDate( creditLimitMaster, hdl );
  insertReviewDate( creditLimitMaster, data, hdl );
  updateLastAndNextReviewDateFields( creditLimitMaster, data, hdl );
}


/*===================================================================================
  GET IDENTITY ON CREDIT LIMIT
  ===================================================================================*/


void KNCB_CreditLimit::onGetByName( char const               *name,
                                    KNET_RequestHandle const &handle )
{
  KNDB_LOOP_ONCE_BEGIN

  try
    {
      KNDB_T_READ
      KNCB_CreditLimit::RELATED_PS_CLASS_VAR psObject
      = KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->queryName(name,"1=1");
      if (PS_is_nil(psObject))
        {
          throw_NOTFOUND(KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->className());
        }

      if( !RELATED_PS_FACTORY::instance()->hasAccess( true, false, psObject,
          toPS( handle->getUser() ) ) )
        throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);

      if(!PS_is_nil(psObject->arcCptyCoverage()) &&
          !Cpty_Factory::instance()->hasAccess(2,true, false,psObject->arcCptyCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }
      if(!PS_is_nil(psObject->arcFolderCoverage()) &&
          !Folder_Factory::instance()->hasAccess(2,true, false,psObject->arcFolderCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }

      KNCB_CreditLimit::RELATED_KNET_CLASS_ACCESS knetObject;

      PSToKNET(psObject,knetObject);
      KNDB_T_COMMIT
      //KNCB_CreditLimit::RELATED_VALIDATION_RESPONSE_CLASS::sendGetSuccess(knetObject, handle);
      //KGL_DataResponse<KNCB_CreditLimit::RELATED_KNET_CLASS_ACCESS>::sendSuccess(knetObject, KNC_FailureCategory::NO_FAILURE, 0, handle);
      KNC_Result res=KGL_DataResponse::sendSuccess( knetObject, handle );
      if(!res)
        {
          throw_LOGICAL(res.text());
        };
      return;
    }
  catch (const PS_UserError& e)
    {
      KNDB_T_ROLLBACK
      ERROR_LOG << e.description() << std::endl ;
	  this->failure(e, handle);
      return;
    }
  catch (const PS_ServerError& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
		  this->failure(e, handle);
          return;
        }
    }
  KNDB_LOOP_END
}

void
KNCB_CreditLimit::onGetByShortName(char const* shortName,
                                   KNET_RequestHandle const & handle)
{
  //kncbtkCreditLimitIdentity_.getByShortName(shortName,handle);

  KNDB_LOOP_ONCE_BEGIN
  try
    {
      KNDB_T_READ
      KNCB_CreditLimit::RELATED_PS_CLASS_VAR psObject
      = KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->queryShortName(shortName,"1=1");
      if (PS_is_nil(psObject))
        {
          throw_NOTFOUND(KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->className());
        }
      KNCB_CreditLimit::RELATED_KNET_CLASS_ACCESS knetObject;

      if( !RELATED_PS_FACTORY::instance()->hasAccess( true, false, psObject,
          toPS( handle->getUser() ) ) )
        throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);

      if(!PS_is_nil(psObject->arcCptyCoverage()) &&
          !Cpty_Factory::instance()->hasAccess(2,true, false,psObject->arcCptyCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }
      if(!PS_is_nil(psObject->arcFolderCoverage()) &&
          !Folder_Factory::instance()->hasAccess(2,true, false,psObject->arcFolderCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }

      PSToKNET(psObject,knetObject);
      KNDB_T_COMMIT
      //KGL_DataResponse<KNCB_CreditLimit::RELATED_KNET_CLASS_ACCESS>::sendSuccess(knetObject, KNC_FailureCategory::NO_FAILURE, 0, handle);
      KNC_Result res=KGL_DataResponse::sendSuccess(knetObject, handle);
      if(!res)
        {
          throw_LOGICAL(res.text());
        };
      return;
    }
  catch (const PS_UserError& e)
    {
      KNDB_T_ROLLBACK
      ERROR_LOG << e.description() << std::endl ;
	  this->failure(e, handle);
      return;
    }
  catch (const PS_ServerError& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
		  this->failure(e, handle);
          return;
        }
    }
  KNDB_LOOP_END

}

void
KNCB_CreditLimit::onQueryIdentityByShortName( char const               *shortName,
    KNET_Limit::LimitKind    *limitKind,
    int                       maxLength,
    KNET_RequestHandle const &handle )
{
  //kncbtkLimitIdentity_.queryIdentityByShortName(shortName, maxLength, handle);


  KGR_Collection<KNET_Identity> identityCollection;

  KNDB_LOOP_ONCE_BEGIN

  try
    {

      //KNDB_T_READ
      //		KNCB_SET_MAX_ROW_BEGIN(maxLength)
      int totalCount=0;

      PS_Oid_var userOid(new PS_Oid);
      try
        {
          userOid->setOidVal((const unsigned char*)(handle->getUser()).getValue());
        }
      catch (const PS_UserError& e)
        {
			ERROR_LOG << e.description() << endl;
        }
      catch (const PS_ServerError& e)
        {
			ERROR_LOG << e.description << endl;
        }

      string condition;
      if( limitKind )
        condition = "LimitKind=''" + KNETToPSLimitKind( *limitKind ) + "''";
      else
        condition = "1=1";

      CreditLimitMaster_Coll_var cltn
      = RELATED_PS_FACTORY::instance()->queryLikeShortName( shortName,
          condition.c_str(),
          maxLength,
          totalCount,
          userOid );
      //		KNCB_SET_MAX_ROW_END
      totalCount=cltn->size();

      if (totalCount==0)
        {
          throw_NOTFOUND(KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->className());
        }

      //KNCB_CreditLimit::RELATED_PS_CLASS_CLTN_VAR cltn;
      //cltn=iter->nextBatch(maxLength);


      unsigned long i= (int) 0.0;

      CreditLimitMaster_Coll::iterator pt =cltn->begin();

      for (i = 0; i < cltn->size(); ++i)
        {
          if (identityCollection.size() >=  (unsigned long)maxLength)
            i=cltn->size()+1;

	  //Bug 7345 - Access test are done in QueryUltraData by call of AccessibleDataFetcher on Cpty then on Folder

          identityCollection.push_back(KNET_Identity((*pt)->ShortName()
                                       ,(*pt)->Name()
                                       ,KGR_Id((*pt)->Id()->getOidVal())));
          pt++;
        }


      if( identityCollection.size() == 0 )
        throw_NOTFOUND(KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->className());

      //KNDB_T_COMMIT
      KNC_Result res=KGL_DataCollResponse<KNET_Identity>::sendSuccess(identityCollection,totalCount,handle);
      if(!res)
        {
          throw_LOGICAL(res.text());
        };
    }
  catch (const PS_UserError& e)
    {
      KNDB_T_ROLLBACK
      ERROR_LOG << e.description() << std::endl ;
	  this->failure(e, handle);
      return;
    }
  catch (const PS_ServerError& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
		  this->failure(e, handle);
          return;
        }
    }
  KNDB_LOOP_END
}

void KNCB_CreditLimit::onQueryIdentityByName( char const               *name,
    KNET_Limit::LimitKind    *limitKind,
    int                       maxLength,
    KNET_RequestHandle const &handle )
{
  //kncbtkLimitIdentity_.queryIdentityByName(name, maxLength, handle);

  KGR_Collection<KNET_Identity> identityCollection;

  KNDB_LOOP_ONCE_BEGIN
  try
    {

      //KNDB_T_READ
      //		KNCB_SET_MAX_ROW_BEGIN(maxLength)
      int totalCount=0;

      PS_Oid_var userOid(new PS_Oid);
      try
        {
          userOid->setOidVal((const unsigned char*)(handle->getUser()).getValue());
        }
      catch (const PS_UserError& e)
        {
			ERROR_LOG << e.description() << endl;
        }
      catch (const PS_ServerError& e)
        {
			ERROR_LOG << e.description << endl;
        }

      string condition;
      if( limitKind )
        condition = "LimitKind=''" + KNETToPSLimitKind( *limitKind ) + "''";
      else
        condition = "1=1";

      CreditLimitMaster_Coll_var cltn
      = RELATED_PS_FACTORY::instance()->queryLikeName( name,
          condition.c_str(),
          maxLength,
          totalCount,userOid);

      //		KNCB_SET_MAX_ROW_END
      totalCount=cltn->size();

      if (totalCount==0)
        {
          throw_NOTFOUND(KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->className());
        }

      //KNCB_CreditLimit::RELATED_PS_CLASS_CLTN_VAR cltn;
      //cltn=iter->nextBatch(maxLength);


      unsigned long i= (int) 0.0;

      /*typename*/
      CreditLimitMaster_Coll::iterator pt =cltn->begin();

      for (i = 0; i < cltn->size(); ++i)
        {
          if (identityCollection.size() >=  (unsigned long)maxLength)
            i=cltn->size()+1;

	  //Bug 7345 - Access test are done in QueryUltraData by call of AccessibleDataFetcher on Cpty then on Folder

	  /*

          if(!PS_is_nil((*pt)->arcCptyCoverage()) &&
              !Cpty_Factory::instance()->hasAccess(2,true, false,(*pt)->arcCptyCoverage(),toPS( handle->getUser() )))
            {
              pt++;
              continue;
            }
          if(!PS_is_nil((*pt)->arcFolderCoverage()) &&
              !Folder_Factory::instance()->hasAccess(2,true, false,(*pt)->arcFolderCoverage(),toPS( handle->getUser() )))
            {
              pt++;
              continue;
            }
	  */

          identityCollection.push_back(KNET_Identity((*pt)->ShortName()
                                       ,(*pt)->Name()
                                       ,KGR_Id((*pt)->Id()->getOidVal())));
          pt++;

        }

      if( identityCollection.size() == 0 )
        throw_NOTFOUND(KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->className());

      //	KNDB_T_COMMIT
      KNC_Result res=KGL_DataCollResponse<KNET_Identity>::sendSuccess(identityCollection,totalCount,handle);
      if(!res)
        {
          throw_LOGICAL(res.text());
        };
    }
  catch (const PS_UserError& e)
    {
      KNDB_T_ROLLBACK
      ERROR_LOG << e.description() << std::endl ;
	  this->failure(e, handle);
      return;
    }
  catch (const PS_ServerError& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
		  this->failure(e, handle);
          return;
        }
    }
  KNDB_LOOP_END
}


void
KNCB_CreditLimit::onGetVDVIdentityByName( char const               *name,
    KNET_Limit::LimitKind    *limitKind,
    KNET_RequestHandle const &handle )
{
  KNDB_LOOP_ONCE_BEGIN
  try
    {
      KNDB_T_READ

      string condition;
      if( limitKind )
        condition = "LimitKind='" + KNETToPSLimitKind( *limitKind ) + "' AND UseVDV = 1";
      else
        condition = "UseVDV = 1";

      KNCB_CreditLimit::RELATED_PS_CLASS_VAR CreditLimitMaster_var
      = RELATED_PS_FACTORY::instance()->queryName(name,condition.c_str());

      if( PS_is_nil( CreditLimitMaster_var )   ||
          CreditLimitMaster_var->UseVDV() == 0 ||
          ( limitKind &&
            *limitKind != PSToKNETLimitKind( CreditLimitMaster_var->LimitKind() ) ) )
        {
          //KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND,"", handle);
          throw_NOTFOUND(KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->className());
        }

      if(!CreditLimitMaster_Factory::instance()->hasAccess(false,true,CreditLimitMaster_var,toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }
      if(!PS_is_nil(CreditLimitMaster_var->arcCptyCoverage()) &&
          !Cpty_Factory::instance()->hasAccess(2,false,true,CreditLimitMaster_var->arcCptyCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }
      if(!PS_is_nil(CreditLimitMaster_var->arcFolderCoverage()) &&
          !Folder_Factory::instance()->hasAccess(2,false,true,CreditLimitMaster_var->arcFolderCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }


      KNDB_T_COMMIT

      KNET_Identity knetObject( CreditLimitMaster_var->ShortName(),
                                CreditLimitMaster_var->Name(),
                                KGR_Id( CreditLimitMaster_var->Id()->getOidVal() ) );

      KNC_Result res = KGL_DataResponse::sendSuccess( knetObject, handle );

      if( !res )
        throw_LOGICAL( res.text() );
    }
  catch (const PS_UserError& e)
    {
      KNDB_T_ROLLBACK
      ERROR_LOG << e.description() << std::endl ;
	  this->failure(e, handle);
      return;
    }
  catch (const PS_ServerError& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE = KNDB_HANDLE_EXCEPTION( e );
      if( !kncResultHE )
        {
          ERROR_LOG << e.description << std::endl ;
		  this->failure(e, handle);
          return;
        }
    }
  KNDB_LOOP_END
}


void
KNCB_CreditLimit::onGetVDVIdentityByShortName( char const               *shortName,
    KNET_Limit::LimitKind    *limitKind,
    KNET_RequestHandle const &handle )
{
  KNDB_LOOP_ONCE_BEGIN
  try
    {
      KNDB_T_READ

      string condition;
      if( limitKind )
        condition = "LimitKind='" + KNETToPSLimitKind( *limitKind ) + "' AND UseVDV = 1";
      else
        condition = "UseVDV = 1";

      KNCB_CreditLimit::RELATED_PS_CLASS_VAR CreditLimitMaster_var
      = RELATED_PS_FACTORY::instance()->queryShortName( shortName,condition.c_str());

      if( PS_is_nil( CreditLimitMaster_var )   ||
          CreditLimitMaster_var->UseVDV() == 0 ||
          ( limitKind &&
            *limitKind != PSToKNETLimitKind( CreditLimitMaster_var->LimitKind() ) ) )
        {
          //KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND,"", handle);
          throw_NOTFOUND(KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->className());
        }


      if(!CreditLimitMaster_Factory::instance()->hasAccess(false,true,CreditLimitMaster_var,toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }
      if(!PS_is_nil(CreditLimitMaster_var->arcCptyCoverage()) &&
          !Cpty_Factory::instance()->hasAccess(2,false,true,CreditLimitMaster_var->arcCptyCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }
      if(!PS_is_nil(CreditLimitMaster_var->arcFolderCoverage()) &&
          !Folder_Factory::instance()->hasAccess(2,false,true,CreditLimitMaster_var->arcFolderCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITWRITE_ERROR_MSG);
        }

      KNDB_T_COMMIT

      KNET_Identity knetObject( CreditLimitMaster_var->ShortName(),
                                CreditLimitMaster_var->Name(),
                                KGR_Id( CreditLimitMaster_var->Id()->getOidVal() ) );

      KNC_Result res = KGL_DataResponse::sendSuccess( knetObject, handle );

      if( !res )
        throw_LOGICAL( res.text() );
    }
  catch (const PS_UserError& e)
    {
      KNDB_T_ROLLBACK
      ERROR_LOG << e.description() << std::endl ;
	  this->failure(e, handle);
      return;
    }
  catch (const PS_ServerError& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE = KNDB_HANDLE_EXCEPTION( e );
      if( !kncResultHE )
        {
          ERROR_LOG << e.description << std::endl ;
		  this->failure(e, handle);
          return;
        }
    }
  KNDB_LOOP_END
}


void
KNCB_CreditLimit::onQueryVDVIdentityByName( char const               *name,
    KNET_Limit::LimitKind    *limitKind,
    int                       maxLength,
    KNET_RequestHandle const &handle )
{

  KGR_Collection<KNET_Identity> identityCollection;

  KNDB_LOOP_ONCE_BEGIN

  try
    {
      //KNDB_T_READ
      //		KNCB_SET_MAX_ROW_BEGIN( maxLength )

      int totalCount = 0;

      PS_Oid_var userOid( new PS_Oid );
      try
        {
          userOid->setOidVal( (const unsigned char*)(handle->getUser()).getValue());
        }
      catch (const PS_UserError& e)
        {
			ERROR_LOG << e.description() << endl;
        }
      catch (const PS_ServerError& e)
        {
			ERROR_LOG << e.description << endl;
        }

      string condition;
      if( limitKind )
        condition = "LimitKind='" + KNETToPSLimitKind( *limitKind ) + "' AND UseVDV = 1";
      else
        condition = "UseVDV = 1";

      CreditLimitMaster_Coll_var cltn
      = RELATED_PS_FACTORY::instance()->queryLikeName( name,
          condition.c_str(),
          maxLength,
          totalCount,
          userOid );
      //		KNCB_SET_MAX_ROW_END
      totalCount=cltn->size();

      if( totalCount == 0 )
        throw_NOTFOUND(KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->className());

      unsigned long i= (int) 0.0;

      CreditLimitMaster_Coll::iterator pt =cltn->begin();

      for( i = 0; i < cltn->size(); ++i )
        {
          if (identityCollection.size() >= (unsigned long)maxLength)
            i=cltn->size()+1;
          if(!PS_is_nil((*pt)->arcCptyCoverage()) &&
              !Cpty_Factory::instance()->hasAccess(2,true, false,(*pt)->arcCptyCoverage(),toPS( handle->getUser() )))
            {
              pt++;
              continue;
            }
          if(!PS_is_nil((*pt)->arcFolderCoverage()) &&
              !Folder_Factory::instance()->hasAccess(2,true, false,(*pt)->arcFolderCoverage(),toPS( handle->getUser() )))
            {
              pt++;
              continue;
            }

          identityCollection.push_back(KNET_Identity((*pt)->ShortName()
                                       ,(*pt)->Name()
                                       ,KGR_Id((*pt)->Id()->getOidVal())));
          pt++;
        }

      if( identityCollection.size() == 0 )
        throw_NOTFOUND(KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->className());

      //KNDB_T_COMMIT
      KNC_Result res=KGL_DataCollResponse<KNET_Identity>::sendSuccess(identityCollection,totalCount,handle);
      if(!res)
        {
          throw_LOGICAL(res.text());
        };
    }
  catch (const PS_UserError& e)
    {
      KNDB_T_ROLLBACK
      ERROR_LOG << e.description() << std::endl ;
	  this->failure(e, handle);
      return;
    }
  catch (const PS_ServerError& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
		  this->failure(e, handle);
          return;
        }
    }
  KNDB_LOOP_END
}


void
KNCB_CreditLimit::onQueryVDVIdentityByShortName( char const               *shortName,
    KNET_Limit::LimitKind    *limitKind,
    int                       maxLength,
    KNET_RequestHandle const &handle )
{

  KGR_Collection<KNET_Identity> identityCollection;

  KNDB_LOOP_ONCE_BEGIN

  try
    {
      //KNDB_T_READ
      //		KNCB_SET_MAX_ROW_BEGIN( maxLength )

      int totalCount = 0;

      PS_Oid_var userOid( new PS_Oid );
      try
        {
          userOid->setOidVal( (const unsigned char*)(handle->getUser()).getValue());
        }
      catch (const PS_UserError& e)
        {
			ERROR_LOG << e.description() << endl;
        }
      catch (const PS_ServerError& e)
        {
			ERROR_LOG << e.description << endl;
        }

      string condition;
      if( limitKind )
        condition = "LimitKind='" + KNETToPSLimitKind( *limitKind ) + "' AND UseVDV = 1";
      else
        condition = "UseVDV = 1";

      CreditLimitMaster_Coll_var cltn
      = RELATED_PS_FACTORY::instance()->queryLikeShortName( shortName,
          condition.c_str(),
          maxLength,
          totalCount,
          userOid );
      //		KNCB_SET_MAX_ROW_END
      totalCount=cltn->size();

      if( totalCount == 0 )
        throw_NOTFOUND(KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->className());

      unsigned long i= (int) 0.0;

      CreditLimitMaster_Coll::iterator pt =cltn->begin();

      for( i = 0; i < cltn->size(); ++i )
        {
          if (identityCollection.size() >= (unsigned long)maxLength)
            i=cltn->size()+1;
          if(!PS_is_nil((*pt)->arcCptyCoverage()) &&
              !Cpty_Factory::instance()->hasAccess(2,true, false,(*pt)->arcCptyCoverage(),toPS( handle->getUser() )))
            {
              pt++;
              continue;
            }
          if(!PS_is_nil((*pt)->arcFolderCoverage()) &&
              !Folder_Factory::instance()->hasAccess(2,true, false,(*pt)->arcFolderCoverage(),toPS( handle->getUser() )))
            {
              pt++;
              continue;
            }

          identityCollection.push_back(KNET_Identity((*pt)->ShortName()
                                       ,(*pt)->Name()
                                       ,KGR_Id((*pt)->Id()->getOidVal())));
          pt++;
        }

      if( identityCollection.size() == 0 )
        throw_NOTFOUND(KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->className());

      //KNDB_T_COMMIT
      KNC_Result res=KGL_DataCollResponse<KNET_Identity>::sendSuccess(identityCollection,totalCount,handle);
      if(!res)
        {
          throw_LOGICAL(res.text());
        };
    }
  catch (const PS_UserError& e)
    {
      KNDB_T_ROLLBACK
      ERROR_LOG << e.description() << std::endl ;
	  this->failure(e, handle);
      return;
    }
  catch (const PS_ServerError& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
		  this->failure(e, handle);
          return;
        }
    }
  KNDB_LOOP_END
}


void
KNCB_CreditLimit::onGetIdentityByName( char const               *name,
                                       KNET_Limit::LimitKind    *limitKind,
                                       KNET_RequestHandle const &handle )
{
  KNDB_LOOP_ONCE_BEGIN
  try
    {
      KNDB_T_READ

      string condition;
      if( limitKind )
        condition = "LimitKind='" + KNETToPSLimitKind( *limitKind ) + "'";
      else
        condition = "1=1";

      KNCB_CreditLimit::RELATED_PS_CLASS_VAR CreditLimitMaster_var
      = RELATED_PS_FACTORY::instance()->queryName(name,condition.c_str());

      if( PS_is_nil( CreditLimitMaster_var ) ||
          ( limitKind &&
            *limitKind != PSToKNETLimitKind( CreditLimitMaster_var->LimitKind() ) ) )
        {
          //KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND,"", handle);
          throw_NOTFOUND(KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->className());
        }


      if(!CreditLimitMaster_Factory::instance()->hasAccess(true,false,CreditLimitMaster_var,toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }
      if(!PS_is_nil(CreditLimitMaster_var->arcCptyCoverage()) &&
          !Cpty_Factory::instance()->hasAccess(2,true,false,CreditLimitMaster_var->arcCptyCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }
      if(!PS_is_nil(CreditLimitMaster_var->arcFolderCoverage()) &&
          !Folder_Factory::instance()->hasAccess(2,true,false,CreditLimitMaster_var->arcFolderCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }

      KNDB_T_COMMIT

      KNET_Identity knetObject(CreditLimitMaster_var->ShortName()
                               ,CreditLimitMaster_var->Name()
                               ,KGR_Id(CreditLimitMaster_var->Id()->getOidVal()));

      KNC_Result res=KGL_DataResponse::sendSuccess(knetObject, handle);
      if(!res)
        {
          throw_LOGICAL(res.text());
        };
    }
  catch (const PS_UserError& e)
    {
      KNDB_T_ROLLBACK
      ERROR_LOG << e.description() << std::endl ;
	  this->failure(e, handle);
      return;
    }
  catch (const PS_ServerError& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
		  this->failure(e, handle);
          return;
        }
    }
  KNDB_LOOP_END
}

void
KNCB_CreditLimit::onGetIdentityByShortName( char const               *shortName,
    KNET_Limit::LimitKind    *limitKind,
    KNET_RequestHandle const &handle )
{

  KNDB_LOOP_ONCE_BEGIN
  try
    {
      KNDB_T_READ

      string condition;
      if( limitKind )
        condition = "LimitKind='" + KNETToPSLimitKind( *limitKind ) + "'";
      else
        condition = "1=1";

      KNCB_CreditLimit::RELATED_PS_CLASS_VAR CreditLimitMaster
      = RELATED_PS_FACTORY::instance()->queryShortName(shortName,condition.c_str());

      if( PS_is_nil( CreditLimitMaster ) ||
          ( limitKind &&
            *limitKind != PSToKNETLimitKind( CreditLimitMaster->LimitKind() ) ) )
        {
          //KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND,"",  handle);
          throw_NOTFOUND(KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->className());
        }


      if(!CreditLimitMaster_Factory::instance()->hasAccess(true,false,CreditLimitMaster,toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }
      if(!PS_is_nil(CreditLimitMaster->arcCptyCoverage()) &&
          !Cpty_Factory::instance()->hasAccess(2,true,false,CreditLimitMaster->arcCptyCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }
      if(!PS_is_nil(CreditLimitMaster->arcFolderCoverage()) &&
          !Folder_Factory::instance()->hasAccess(2,true,false,CreditLimitMaster->arcFolderCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }

      KNDB_T_COMMIT

      KNET_Identity knetObject(CreditLimitMaster->ShortName()
                               ,CreditLimitMaster->Name()
                               ,KGR_Id(CreditLimitMaster->Id()->getOidVal()));

      KNC_Result res=KGL_DataResponse::sendSuccess(knetObject, handle);
      if(!res)
        {
          throw_LOGICAL(res.text());
        };

    }
  catch (const PS_UserError& e)
    {
      KNDB_T_ROLLBACK
      ERROR_LOG << e.description() << std::endl ;
	  this->failure(e, handle);
      return;
    }
  catch (const PS_ServerError& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
		  this->failure(e, handle);
          return;
        }
    }
  KNDB_LOOP_END

  //onGetReviewDateMessages(handle) ;

}

void
KNCB_CreditLimit::onGetIdentityByIdentifier( KGR_Id const       &id,
    KNET_RequestHandle  handle )
{
  KNDB_LOOP_ONCE_BEGIN
  try
    {
      KNDB_T_READ

      KNCB_CreditLimit::RELATED_PS_CLASS_VAR CreditLimitMaster =
        KNCBTK_CoreBasic< KNCB_CreditLimit::RELATED_PS_CLASS_VAR,
        KNCB_CreditLimit::RELATED_PS_FACTORY >::queryId( id );

      if( PS_is_nil( CreditLimitMaster ) )
        throw_NOTFOUND(KNCB_CreditLimit::RELATED_PS_FACTORY::instance()->className());

      if(!CreditLimitMaster_Factory::instance()->hasAccess(true,false,CreditLimitMaster,toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }
      if(!PS_is_nil(CreditLimitMaster->arcCptyCoverage()) &&
          !Cpty_Factory::instance()->hasAccess(2,true,false,CreditLimitMaster->arcCptyCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }
      if(!PS_is_nil(CreditLimitMaster->arcFolderCoverage()) &&
          !Folder_Factory::instance()->hasAccess(2,true,false,CreditLimitMaster->arcFolderCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }
      KNDB_T_COMMIT

      KNET_Identity knetObject( CreditLimitMaster->ShortName(),
                                CreditLimitMaster->Name(),
                                KGR_Id(CreditLimitMaster->Id()->getOidVal() ) );

      KNC_Result res = KGL_DataResponse::sendSuccess( knetObject, handle );
      if( !res )
        throw_LOGICAL( res.text() );
    }
  catch (const PS_UserError& e)
    {
      KNDB_T_ROLLBACK
      ERROR_LOG << e.description() << std::endl ;
	  this->failure(e, handle);
      return;
    }
  catch (const PS_ServerError& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
		  this->failure(e, handle);
          return;
        }
    }
  KNDB_LOOP_END
}


void
KNCB_CreditLimit::queryLimitReviewMessage(KNET_RequestHandle handle)
{
  KGLDB_WhereClause whereClause;
  CreditLimitMaster_var CLMaster;
  ReviewCredElt_var reviewCredElt;


	//ReviewerId =KNUserId OR EXISTS (SELECT 1 FROM LinkedKNUser WHERE KNUserIdParent = ReviewerId AND KNUserIdChild = KNUserId)
	string clause;
	whereClause.addCondition( " ReviewerId", "=", handle->getUser() );
	clause = whereClause.getConditions();
	whereClause.erase();
	whereClause.addCondition( " KNUserIdChild", "=", handle->getUser() );

	clause.append("  OR EXISTS (SELECT 1 FROM LinkedKNUser WHERE KNUserIdParent = CreditLimitMaster.ReviewerId AND ");
	clause.append(whereClause.getConditions());
	clause.append(")");


  CreditLimitMaster_Cltn_var psCreditLimitMasterCltn = CreditLimitMaster_Factory::instance()->querySQLWhere(clause.c_str());

  KNC_Date today(KNC_ConvDate::getNow()) ;

  KGR_Date knettoday ;
  knettoday.setDate(today);

  int index, size = 0;
  if(!PS_is_nil(psCreditLimitMasterCltn))
      size = psCreditLimitMasterCltn->length();
  for(index = 0 ; index < size ; ++index)
    {
      CLMaster = psCreditLimitMasterCltn[(unsigned long)index];

      //conversion date persitence KNC_Date
      KNC_Date date ;
      date.strToDate(CLMaster->NextReviewDate());

      if(date1lesseq2(date,today))  // la nextReviewDate est aujourdhui ou est passee ?
        {
          //ajout a la collection du message
          whereClause.erase();

          whereClause.addCondition( "CreditLimitMasterId", "=", CLMaster->Id() );

          whereClause.addCondition( "ReviewDate", "=", CLMaster->NextReviewDate() );

          // tous les messages compris entre la derniere date de review et aujourdhui.
          //whereClause.addCondition("ReviewDate", ">=", CLMaster->NextReviewDate());
          //whereClause.addCondition("ReviewDate", "<", KNET_DateToPS(knettoday).c_str());


          ReviewCredElt_Cltn_var psReviewDateCltn = ReviewCredElt_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());

          //on n'affiche qu'un seul message...mais doit afficher une collection de message.
			unsigned long size = 0;
	         if(!PS_is_nil(psReviewDateCltn))
	              size = psReviewDateCltn->length();
             if(size)
            {
              reviewCredElt = psReviewDateCltn[size-1];

            }

        }
    }

}


  /*===================================================================================
  Link
  ===================================================================================*/

/** */
void
KNCB_CreditLimit::onLink (KGR_Id const& parent,
						 KGR_Id const& child,
						 bool creditLimitLinkHierarchy,
						 KNET_RequestHandle handle)
{

  kncbtkCreditLimitMasterLink_.onLink(parent,
  								child,
  									creditLimitLinkHierarchy,
  									//netToParent,
  									//ownedPart,
  									handle);
}

/** */
void
KNCB_CreditLimit::onUnlink (KGR_Id const& parent,
						   KGR_Id const& child,
						   KNET_RequestHandle handle)
{

	kncbtkCreditLimitMasterLink_.onUnlink(parent, child, handle);
}

/** */
void
KNCB_CreditLimit::onIsChild (KGR_Id const& id,
						 KNET_RequestHandle handle)
{

	kncbtkCreditLimitMasterLink_.onIsChild(id, handle);
}

/** */
void
KNCB_CreditLimit::onUpdateLink (KGR_Id const& parent,
							   KGR_Id const& child,
							   bool creditLimitLinkHierarchy,
						 		KNET_RequestHandle handle)
{

  kncbtkCreditLimitMasterLink_.onUpdateLink(parent
  					   ,child
  					   	, creditLimitLinkHierarchy
  						   ,handle);
}


/*
 * onQueryDirectChildren (KNET_Id...)
 */
void
KNCB_CreditLimit::onQueryDirectChildren(KGR_Id const& parent,
								 int maxLength,
								 KNET_RequestHandle handle)
{

  kncbtkCreditLimitMasterLink_.onQueryDirectChildren(parent, maxLength, handle);
}
/*
 * onQueryDirectChildren (KNET_Alias...)
 */
void
KNCB_CreditLimit::onQueryDirectChildren(KGR_Alias const& parent,
								 int maxLength,
								 KNET_RequestHandle handle)
{
}

/*
 * onQueryDirectParents (KNET_Id...)
 */
void
KNCB_CreditLimit::onQueryDirectParents(KGR_Id const& child,
								int maxLength,
								KNET_RequestHandle handle)
{

  kncbtkCreditLimitMasterLink_.onQueryDirectParents(child, maxLength, handle);
}
/*
 * onQueryDirectParents (KNET_Alias...)
 */
void
KNCB_CreditLimit::onQueryDirectParents(KGR_Alias const& child,
								int maxLength,
								KNET_RequestHandle handle)
{
}

/*
 * onQueryChildren (KNET_Id...)
 */
void
KNCB_CreditLimit::onQueryChildren(KGR_Id const& parent,
						   KNET_RequestHandle handle )
{

	  kncbtkCreditLimitMasterLink_.onQueryChildren(parent, handle);
}
/*
 * onQueryChildren (KNET_Alias...)
 */
void
KNCB_CreditLimit::onQueryChildren(KGR_Alias const& parent,
						   KNET_RequestHandle handle )
{
}

/*
 * onQueryParents (KNET_Id...)
 */
void
KNCB_CreditLimit::onQueryParents(KGR_Id const& child,
						  KNET_RequestHandle handle)
{

	  kncbtkCreditLimitMasterLink_.onQueryParents(child, handle);
}
/*
 * onQueryParents (KNET_Alias...)
 */
void
KNCB_CreditLimit::onQueryParents(KGR_Alias const& child,
						  KNET_RequestHandle handle)
{
}

/*
* getKNETLinkFromPS
*/
KNET_CreditLimitLink
KNCB_CreditLimit::getKNETLinkFromPS(KNET_Identity const& identity, CreditLimitMasterLink_var const& psObject, bool isChild )
{
	KH_DBG::dbg("KNCB_CreditLimit::getKNETLinkFromPS::method_start");
	double allocatedAmount=0;
	double usedAmount=0;
	KNET_Identity currencyIdentity;


	KNET_CreditLimitLink knetLink(identity
								  ,psObject->LinkHierarchy()
		);

	PS_Oid_var psLimitId(new PS_Oid);

	if(isChild)
		psLimitId = psObject->ChildId();
	else
		psLimitId = psObject->ParentId();

	currencyIdentity = getCurrency(psLimitId);
	allocatedAmount= getAllocatedAmount(psLimitId);
	usedAmount = getUsedAmount(psLimitId);

	knetLink.setAllocatedAmount(allocatedAmount);
	knetLink.setCurrency(currencyIdentity);
	knetLink.setUsedAmount(usedAmount);
	KH_DBG::dbg("KNCB_CreditLimit::getKNETLinkFromPS::method_end");
	return knetLink;
}

/*
* topKNETLinkInstance
*/
KNET_CreditLimitLink
KNCB_CreditLimit::topKNETLinkInstance(KNET_Identity const& identity)
{
	double allocatedAmount=0;
	double usedAmount=0;
	KNET_Identity currencyIdentity;

	KNET_CreditLimitLink knetLink(identity,1);

	CreditLimitMaster_var CLM;
	CreditLimitMasterLink_var link;
	PS_Oid_var psLimitId(new PS_Oid);

    	CLM = RELATED_PS_FACTORY::instance()->queryShortName( identity.getShortName(),"1=1");

	if(!PS_is_nil(CLM))
	{
		KGLDB_WhereClause whereClause1;
		whereClause1.addCondition( "CreditLimitMasterId_Parent", "=", CLM->Id() );

		CreditLimitMasterLink_Cltn_var CLML =
			CreditLimitMasterLink_Factory::instance()->querySQLWhere( whereClause1.getConditions().c_str() );
		int size = 0;
	    if(!PS_is_nil(CLML))
	      size = CLML->length();
	    if(size)
		{
			link = CLML[(unsigned long)0];

			psLimitId = link->ParentId();

			currencyIdentity = getCurrency( psLimitId );
			allocatedAmount= getAllocatedAmount( psLimitId );
			usedAmount = getUsedAmount( psLimitId );

			knetLink.setAllocatedAmount(allocatedAmount);
			knetLink.setCurrency(currencyIdentity);
			knetLink.setUsedAmount(usedAmount);
		}
		else
		{
			currencyIdentity = getCurrency(CLM->Id());
			allocatedAmount= getAllocatedAmount(CLM->Id());
			usedAmount = getUsedAmount(CLM->Id());

			knetLink.setAllocatedAmount(allocatedAmount);

			knetLink.setCurrency(currencyIdentity);

			knetLink.setUsedAmount(usedAmount);
		}
	}
	else
	{
		knetLink.setUsedAmount(0);
		knetLink.setAllocatedAmount(0);
	}

	return knetLink;

}

double KNCB_CreditLimit::getUsedAmount(PS_Oid_var const& psObject)
{

	CreditLimit_var CL;
	double used=0;
	KGLDB_WhereClause whereClause1;
	whereClause1.addCondition( "CreditLimitMasterId", "=", psObject );


	CreditLimit_Cltn_var Climit =
	               CreditLimit_Factory::instance()->querySQLWhere( whereClause1.getConditions().c_str() );

	if(!PS_is_nil(Climit))
	{
		unsigned long collSize = Climit->length();
		for ( unsigned long i=0; i<collSize; ++i)
		{
			CL = Climit[i];
			if(used< CL->UsedAmount())
				used=CL->UsedAmount() ;
		}
	}

	return used;
}

double
KNCB_CreditLimit::getAllocatedAmount(PS_Oid_var const& psObject)
{

	double allocatedAmount=0;
	CreditLimitMaster_var psCreditLimitMaster;


	KGLDB_WhereClause whereClause1;
	whereClause1.addCondition( "Id", "=", psObject );

    	CreditLimitMaster_Cltn_var CLM =
                CreditLimitMaster_Factory::instance()->querySQLWhere( whereClause1.getConditions().c_str() );

	int size = 0;
    if(!PS_is_nil(CLM))
      size = CLM->length();
    if(size)
	{
		psCreditLimitMaster = CLM[0ul];
		allocatedAmount=psCreditLimitMaster->AllocatedAmount();
	}

	return allocatedAmount;

}

KNET_Identity
KNCB_CreditLimit::getCurrency(PS_Oid_var const& psObject)
{
	CreditLimitMaster_var psCreditLimitMaster;
	Currency_var psCurrency;

	KNET_Identity ident;

	KGLDB_WhereClause whereClause1;
	whereClause1.addCondition( "Id", "=", psObject );

    	CreditLimitMaster_Cltn_var CLM =
                CreditLimitMaster_Factory::instance()->querySQLWhere( whereClause1.getConditions().c_str() );

	int size = 0;
    if(!PS_is_nil(CLM))
      size = CLM->length();
    if(size)
	{
		psCreditLimitMaster = CLM[(unsigned long)0ul];

		psCurrency = Currency_Factory::instance()->queryKey(*psCreditLimitMaster->CurrencyId(),PS_Defs::k_cacheThenDatabase) ;

		if(!PS_is_nil(psCurrency))
		{

			return(KNET_Identity(psCurrency->ShortName()
                                       ,psCurrency->Name()
                                       ,KGR_Id(psCurrency->Id()->getOidVal())));
		}
	}

	return ident;
}


void
KNCB_CreditLimit::AuditRemoveTBCoverageElt( CreditLimitMaster_var            creditLimitMaster,
										   KNET_RequestHandle               handle )
{

	KH_DBG::dbg("KNCB_CreditLimit::AuditRemoveTBCoverageElt::method_start::with_audit");

	TimeBandCoverageElt_var	TimeBandOldElt;
	TimeBandCoverageElt_Cltn_var TBCoverageCollOld_= creditLimitMaster->arcTimeBandCoverageElts();
	unsigned long size = TBCoverageCollOld_->length();

	for (unsigned long idx1=0; idx1 < size; ++idx1){

		TimeBandOldElt = TBCoverageCollOld_[idx1];
		kntcAudit_->logPrepareDelete(
			(const unsigned char*) handle->getUser().getValue()
			,TimeBandOldElt
			,TimeBandCoverageElt_Factory::instance()->getParentTable()
			,creditLimitMaster->Id()
			,TimeBandCoverageElt_Factory::instance()->getCoverage(creditLimitMaster->Id(),creditLimitMaster->Id())
			);

		KH_DBG::dbg("KH_AUDIT::AUD_START::kntcAudit_->logCommitDeleteImmediate:before_call");
		kntcAudit_->logCommitDeleteImmediate(1,1);
		KH_DBG::dbg("KH_AUDIT:::AUD_STOP::kntcAudit_->logCommitDeleteImmediate:after_call");
		KH_DBG::dbg("KNCB_CreditLimit::AuditRemoveTBCoverageElt::method_end::with_audit");

	}




}

void
KNCB_CreditLimit::AuditInsertTBCoverageElt( CreditLimitMaster_var            creditLimitMaster,
										   KNET_RequestHandle               handle )
{

	KH_DBG::dbg("KNCB_CreditLimit::AuditInsertTBCoverageElt::method_start::with_audit");

	TimeBandCoverageElt_var TimeBandNewElt;
	TimeBandCoverageElt_Cltn_var TBCoverageCollNew_ = creditLimitMaster->arcTimeBandCoverageElts();
	unsigned long size = TBCoverageCollNew_->length();
	for (unsigned long idx2=0; idx2 < size ;++idx2) {
			TimeBandNewElt = TBCoverageCollNew_[idx2];
			KH_DBG::dbg("KH_AUDIT::AUD_START::kntcAudit_->logInsertImmediate::before_call_audit");
			kntcAudit_->logInsertImmediate(
				(const unsigned char*) handle->getUser().getValue()
				,TimeBandNewElt
				,TimeBandCoverageElt_Factory::instance()->getParentTable()
				,creditLimitMaster->Id()
				,TimeBandCoverageElt_Factory::instance()->getCoverage(creditLimitMaster->Id()
				,TimeBandNewElt->TimeBandId())
				,false // desactivate action
			    ,true // write immediate);
				);
			KH_DBG::dbg("KH_AUDIT:::AUD_STOP::kntcAudit_->logInsertImmediate::after_call_audit");
	 }

	KH_DBG::dbg("KNCB_CreditLimit::AuditInsertTBCoverageElt::method_end::with_audit");

}

void
KNCB_CreditLimit::AuditInsertTBAllocationScheduleElt( CreditLimitMaster_var            creditLimitMaster,
										   KNET_RequestHandle               handle )
{

	KH_DBG::dbg("KNCB_CreditLimit::AuditInsertTBAllocationScheduleElt::method_start::with_audit");

	 KGLDB_WhereClause whereClause;
	  whereClause.addCondition("CreditLimitMasterId", "=", creditLimitMaster->Id() );

	  CreditAllocSchedElt_Cltn_var collToRemove =
	    CreditAllocSchedElt_Factory::instance()->querySQLWhere(whereClause.getConditions().c_str());

	  unsigned long idx = 0;

	  for( ; idx < collToRemove->length(); ++idx )
	  {

	    //CreditAllocSchedElt_Factory::instance()->remove
	    //( collToRemove[(unsigned long) idx] );

	    CreditAllocSchedElt_var dd = collToRemove[idx];
	    //CreditAllocSchedElt dd_elt;
	    KNTable_var dd_var;
		kntcAudit_->logInsertImmediate(
			(const unsigned char*) handle->getUser().getValue()
			,	dd_var
			//,CreditAllocSchedElt_Factory::instance()->getParentTable()
			,	dd_var
			,	dd_var->Id()
			//,CreditAllocSchedElt_Factory::instance()->getCoverage(creditLimitMaster->Id(),dd->Id)
			,	"HEADER_STRING"
			,	false // desactivate action
		    ,	true // write immediate);
			);

	  }

	TimeBandCoverageElt_var TimeBandNewElt;
	TimeBandCoverageElt_Cltn_var TBCoverageCollNew_ = creditLimitMaster->arcTimeBandCoverageElts();
	unsigned long size = TBCoverageCollNew_->length();
	for (unsigned long idx2=0; idx2 < size ;++idx2) {
			TimeBandNewElt = TBCoverageCollNew_[idx2];
			KH_DBG::dbg("KH_AUDIT::AUD_START::kntcAudit_->logInsertImmediate::before_call_audit");
			kntcAudit_->logInsertImmediate(
				(const unsigned char*) handle->getUser().getValue()
				,TimeBandNewElt
				,TimeBandCoverageElt_Factory::instance()->getParentTable()
				,creditLimitMaster->Id()
				,TimeBandCoverageElt_Factory::instance()->getCoverage(creditLimitMaster->Id()
				,TimeBandNewElt->TimeBandId())
				,false // desactivate action
			    ,true // write immediate);
				);
			KH_DBG::dbg("KH_AUDIT:::AUD_STOP::kntcAudit_->logInsertImmediate::after_call_audit");
	 }

	KH_DBG::dbg("KNCB_CreditLimit::AuditInsertTBAllocationScheduleElt::method_end::with_audit");

}

void
KNCB_CreditLimit::onGetIdentityByNameDV( char const               *name,
                                       KNET_Limit::LimitKind    *limitKind,
                                       KNET_RequestHandle const &handle )
{

  KNDB_LOOP_ONCE_BEGIN
  try
    {
      KNDB_T_READ

      string condition;
         condition=" Name = '";
         condition+= name;
         condition+="' AND ";
      if( limitKind )
        condition += "LimitKind='" + KNETToPSLimitKind( *limitKind ) + "'";
      else
        condition += "1=1";
         CLMasterDVInsert_var CreditLimitMaster_var;
      CLMasterDVInsert_Cltn_var CLMDV
      = CLMasterDVInsert_Factory::instance()->querySQLWhere(condition.c_str());

		int size = 0;
	    if(!PS_is_nil(CLMDV))
	      size = CLMDV->length();
	    if(size)
      {
               CreditLimitMaster_var = CLMDV[(unsigned long)0];
         }
         else
         {
               throw_NOTFOUND(CLMasterDVInsert_Factory::instance()->className());
         }

      if( PS_is_nil( CreditLimitMaster_var ) ||
          ( limitKind &&
            *limitKind != PSToKNETLimitKind( CreditLimitMaster_var->LimitKind() ) ) )
        {
          //KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND,"", handle);
          throw_NOTFOUND(CLMasterDVInsert_Factory::instance()->className());
        }


      if(!CLMasterDVInsert_Factory::instance()->hasAccess(true,false,CreditLimitMaster_var,toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }
      if(!PS_is_nil(CreditLimitMaster_var->arcCptyCoverage()) &&
          !Cpty_Factory::instance()->hasAccess(2,true,false,CreditLimitMaster_var->arcCptyCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }
      if(!PS_is_nil(CreditLimitMaster_var->arcFolderCoverage()) &&
          !Folder_Factory::instance()->hasAccess(2,true,false,CreditLimitMaster_var->arcFolderCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }

      KNDB_T_COMMIT

      KNET_Identity knetObject(CreditLimitMaster_var->ShortName()
                               ,CreditLimitMaster_var->Name()
                               ,KGR_Id(CreditLimitMaster_var->Id()->getOidVal()));

      KNC_Result res=KGL_DataResponse::sendSuccess(knetObject, handle);
      if(!res)
        {
          throw_LOGICAL(res.text());
        };
    }
  catch (const PS_UserError& e)
    {
      KNDB_T_ROLLBACK
      ERROR_LOG << e.description() << std::endl ;
         this->failure(e, handle);
      return;
    }
  catch (const PS_ServerError& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
                 this->failure(e, handle);
          return;
        }
    }
  KNDB_LOOP_END
}

void
KNCB_CreditLimit::onGetIdentityByShortNameDV( char const               *shortName,
    KNET_Limit::LimitKind    *limitKind,
    KNET_RequestHandle const &handle )
{

  KNDB_LOOP_ONCE_BEGIN
  try
    {
      KNDB_T_READ

      string condition;
         condition=" ShortName = '";
         condition+= shortName;
         condition+="' AND ";
      if( limitKind )
        condition += "LimitKind='" + KNETToPSLimitKind( *limitKind ) + "'";
      else
        condition += "1=1";
         CLMasterDVInsert_var CreditLimitMaster;
      CLMasterDVInsert_Cltn_var CLMDVI
      = CLMasterDVInsert_Factory::instance()->querySQLWhere(condition.c_str());

		int size = 0;
	    if(!PS_is_nil(CLMDVI))
	      size = CLMDVI->length();
	    if(size)
      {
               CreditLimitMaster = CLMDVI[(unsigned long)0];
         }
         else
         {
               throw_NOTFOUND(CLMasterDVInsert_Factory::instance()->className());
         }

      if( PS_is_nil( CreditLimitMaster ) ||
          ( limitKind &&
            *limitKind != PSToKNETLimitKind( CreditLimitMaster->LimitKind() ) ) )
        {
          //KGL_Response::sendFailure(KNC_FailureCategory::NOTFOUND,"",  handle);
          throw_NOTFOUND(CLMasterDVInsert_Factory::instance()->className());
        }


      if(!CLMasterDVInsert_Factory::instance()->hasAccess(true,false,CreditLimitMaster,toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }
      if(!PS_is_nil(CreditLimitMaster->arcCptyCoverage()) &&
          !Cpty_Factory::instance()->hasAccess(2,true,false,CreditLimitMaster->arcCptyCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }
      if(!PS_is_nil(CreditLimitMaster->arcFolderCoverage()) &&
          !Folder_Factory::instance()->hasAccess(2,true,false,CreditLimitMaster->arcFolderCoverage(),toPS( handle->getUser() )))
        {
          throw_LOGICAL(NOACCESSLIMITREAD_ERROR_MSG);
        }

      KNDB_T_COMMIT

      KNET_Identity knetObject(CreditLimitMaster->ShortName()
                               ,CreditLimitMaster->Name()
                               ,KGR_Id(CreditLimitMaster->Id()->getOidVal()));
               INFO_LOG <<"sendSuccess"<<std::endl;
      KNC_Result res=KGL_DataResponse::sendSuccess(knetObject, handle);
      if(!res)
        {
          throw_LOGICAL(res.text());
        };

    }
  catch (const PS_UserError& e)
    {
      KNDB_T_ROLLBACK
      ERROR_LOG << e.description() << std::endl ;
         this->failure(e, handle);
      return;
    }
  catch (const PS_ServerError& e)
    {
      KNDB_T_ROLLBACK
      KNC_Result kncResultHE
      = KNDB_HANDLE_EXCEPTION(e);
      if (!kncResultHE)
        {
          ERROR_LOG << e.description << std::endl ;
                 this->failure(e, handle);
          return;
        }
    }
  KNDB_LOOP_END

  //onGetReviewDateMessages(handle) ;

}


void KH_DBG::dbg(string ss)
{
	if(KH_DBG::dbg_no_log() == 1)
    {
            //return ;
    }

    //std::cout << std::endl<< "KH_DEB[" << ss << "]" << std::endl;
    //TRACE_LOG << std::endl<< "KH_DEB[" << ss << "]" << std::endl;
    INFO_LOG << std::endl<< "KH_DEB[" << ss << "]" << std::endl;
}

int KH_DBG::dbg_no_log()
{
    static const char*dbg_env = getenv("KH_DEB");
    if(dbg_env)
    {
            return 0;
    }
    else
    {
        return 1;
    }

}

int KH_DBG::is_set_env(string ss)
{
    static const char*dbg_env = getenv(ss.c_str());
    if(dbg_env)
    {
            return 1;
    }
    else
    {
        return 0;
    }

}

/*------------------------------- End ---------------------------------*/

