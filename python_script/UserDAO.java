package com.inspirational.koreaSiGuDong;

import java.util.List;

import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Repository;

@Repository
public interface KoreaSiGuDongDAO {
	public List<KoreaSiGuDong> selectAll();
	public KoreaSiGuDong selectById(
			@Param("id") int id);
	public List<KoreaSiGuDong> selectBySi(
			@Param("si") String si);
	public List<KoreaSiGuDong> selectBySiAndGu(
			@Param("si") String si,
			@Param("gu") String gu);
	public List<KoreaSiGuDong> selectBySiAndGuAndDong(
			@Param("si") String si,
			@Param("gu") String gu,
			@Param("dong") String dong);
}
